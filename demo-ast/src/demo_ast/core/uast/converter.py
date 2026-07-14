import hashlib
from typing import Protocol, Any, Dict, List

from tree_sitter import Tree, Language, Query, Node

from .uast_node import (
    UASTNode, FileNode, Position, ClassNode, FunctionNode, VariableNode, ImportNode
)

def generate_id(file_path: str, start_byte: int, end_byte: int) -> str:
    """Tạo ID duy nhất dựa trên file và tọa độ byte."""
    raw = f"{file_path}:{start_byte}:{end_byte}"
    return hashlib.md5(raw.encode()).hexdigest()

class UASTConverter(Protocol):
    def convert(
            self,
            tree: Tree,
            source_bytes: bytes,
            file_path: str = "",
            additional_meta: dict[str, Any] | None = None) -> UASTNode:
        pass


class SimpleUASTConverter(UASTConverter):
    def __init__(self, language_name: str, language: Language, query: Query):
        self.language_name = language_name
        self.language = language
        self.query = query

    def _create_position(self, point: tuple[int, int]) -> Position:
        return Position(row=point[0], column=point[1])

    def _extract_text(self, node: Node, source_bytes: bytes) -> str:
        # tree-sitter python API: node.text trả về bytes nếu tree được parse kèm source,
        # nếu không ta phải tự cắt từ source_bytes
        if hasattr(node, "text") and node.text is not None:
            return node.text.decode('utf-8', errors='replace')
        return source_bytes[node.start_byte:node.end_byte].decode('utf-8', errors='replace')

    def convert(
            self,
            tree: Tree,
            source_bytes: bytes,
            file_path: str = "",
            additional_meta: dict[str, Any] | None = None
    ) -> UASTNode:
        ts_root = tree.root_node
        
        # 1. Trích xuất tất cả các captures
        # Lưu ý: tree_sitter API có thể trả về dict hoặc list tùy phiên bản
        from tree_sitter import QueryCursor
        captures_raw = QueryCursor(self.query).captures(ts_root)
        
        captures_map: dict[int, list[str]] = dict()
        
        if isinstance(captures_raw, dict):
            # API trả về dạng dict {capture_name: [nodes]}
            for capture_name, nodes in captures_raw.items():
                for node in nodes:
                    if node.id not in captures_map:
                        captures_map[node.id] = []
                    captures_map[node.id].append(capture_name)
        elif isinstance(captures_raw, list):
            # API trả về dạng list [(node, capture_name)]
            for node, capture_name in captures_raw:
                if node.id not in captures_map:
                    captures_map[node.id] = []
                captures_map[node.id].append(capture_name)

        return self.build_uast(ts_root, captures_map, source_bytes, file_path)

    def build_uast(self, root_ts: Node, captures_map: dict[int, list[str]], source_bytes: bytes, file_path: str) -> FileNode:
        # Bộ đệm để hứng các metadata dạng sibling (đứng trước class/function như Javadoc, Decorators)
        metadata_buffer = []

        def traverse(ts_node: Node, current_uast_parent: UASTNode):
            nonlocal metadata_buffer

            captures = captures_map.get(ts_node.id, [])

            # 1. Kiểm tra xem node này có tạo ra khối định nghĩa mới không?
            new_uast_node = None
            for cap in captures:
                if cap.startswith("definition."):
                    new_uast_node = self._create_uast_node(cap, ts_node, source_bytes, file_path)
                    if new_uast_node:
                        new_uast_node.parent_id = current_uast_parent.id
                        current_uast_parent.children.append(new_uast_node)

                        # Xả bộ đệm (áp dụng Javadoc, Decorators đã tích luỹ từ trước)
                        self._apply_buffer(new_uast_node, metadata_buffer)
                        metadata_buffer.clear()
                        break  

            # Xác định context để truyền xuống cho các node con
            active_context = new_uast_node if new_uast_node else current_uast_parent

            # 2. Xử lý các tag metadata hiện tại (name, doc, modifier)
            for cap in captures:
                if not cap.startswith("definition."):
                    text = self._extract_text(ts_node, source_bytes)
                    if cap == "name":
                        active_context.name = text
                    elif cap in ["doc", "comment", "decorator", "modifier"]:
                        if self._is_child_of(ts_node, active_context):
                            # Docstring kiểu Python (nằm TRONG block định nghĩa)
                            self._apply_buffer(active_context, [(cap, text)])
                        else:
                            # Sibling metadata (nằm NGOÀI / TRƯỚC block định nghĩa)
                            metadata_buffer.append((cap, text))

            # 3. Đệ quy xuống các node con
            for child in ts_node.children:
                traverse(child, active_context)

        # Khởi tạo node root của file
        file_node = FileNode(
            id=generate_id(file_path, root_ts.start_byte, root_ts.end_byte),
            start_point=self._create_position(root_ts.start_point),
            end_point=self._create_position(root_ts.end_point),
            start_byte=root_ts.start_byte,
            end_byte=root_ts.end_byte,
            file_path=file_path,
            language=self.language_name
        )

        traverse(root_ts, file_node)

        return file_node

    def _create_uast_node(self, cap: str, ts_node: Node, source_bytes: bytes, file_path: str) -> UASTNode | None:
        kwargs = {
            "id": generate_id(file_path, ts_node.start_byte, ts_node.end_byte),
            "start_point": self._create_position(ts_node.start_point),
            "end_point": self._create_position(ts_node.end_point),
            "start_byte": ts_node.start_byte,
            "end_byte": ts_node.end_byte,
            "file_path": file_path,
            "source_code": self._extract_text(ts_node, source_bytes),
            "language": self.language_name,
        }
        if cap == "definition.class":
            return ClassNode(**kwargs)
        elif cap == "definition.function":
            return FunctionNode(**kwargs)
        elif cap == "definition.variable":
            return VariableNode(**kwargs)
        elif cap == "definition.import":
            return ImportNode(**kwargs)
        
        # Fallback nếu chưa định nghĩa subclass
        kwargs["node_type"] = cap.replace("definition.", "")
        return UASTNode(**kwargs)

    def _apply_buffer(self, node: UASTNode, buffer: list[tuple[str, str]]):
        for cap, text in buffer:
            if cap in ("doc", "comment"):
                node.docstring = (node.docstring + "\n" + text) if node.docstring else text
            elif cap in ("decorator", "modifier"):
                if cap not in node.metadata:
                    node.metadata[cap] = []
                node.metadata[cap].append(text)

    def _is_child_of(self, ts_node: Node, uast_node: UASTNode) -> bool:
        """Kiểm tra xem node TS hiện tại có nằm VÀO TRONG tọa độ của UAST Node hay không"""
        return ts_node.start_byte >= uast_node.start_byte and ts_node.end_byte <= uast_node.end_byte