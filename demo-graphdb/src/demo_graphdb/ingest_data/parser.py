import os
import tree_sitter_python as tspython
from tree_sitter import Language, Parser

def read_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

class PythonParser:
    def __init__(self):
        self.language = Language(tspython.language())
        self.parser = Parser(self.language)

    def _get_docstring(self, node) -> str:
        """Extract docstring from a class or function block."""
        block_node = None
        for child in node.children:
            if child.type == 'block':
                block_node = child
                break
        if block_node and len(block_node.children) > 0:
            first_stmt = block_node.children[0]
            if first_stmt.type == 'expression_statement':
                for sub_child in first_stmt.children:
                    if sub_child.type == 'string':
                        raw_text = sub_child.text.decode('utf-8')
                        if raw_text.startswith('"""') or raw_text.startswith("'''"):
                            return raw_text[3:-3].strip()
                        elif raw_text.startswith('"') or raw_text.startswith("'"):
                            return raw_text[1:-1].strip()
                        return raw_text.strip()
        return ""

    def _find_calls(self, node, calls_list):
        """Recursively search for all call expressions inside a node."""
        if node.type == 'call':
            func_node = node.child_by_field_name('function') or node.children[0]
            if func_node.type == 'identifier':
                calls_list.append(func_node.text.decode('utf-8'))
            elif func_node.type == 'attribute':
                attr_node = func_node.child_by_field_name('attribute')
                if attr_node:
                    calls_list.append(attr_node.text.decode('utf-8'))
                else:
                    calls_list.append(func_node.text.decode('utf-8'))
        for child in node.children:
            self._find_calls(child, calls_list)

    def parse_file(self, file_path: str):
        """
        Parses a python file and extracts structural metadata:
        - file details
        - classes (with their methods)
        - top-level functions
        """
        try:
            code_string = read_file(file_path)
        except Exception as e:
            print(f"[-] Lỗi khi đọc file code {file_path}: {e}")
            return None

        code_bytes = bytes(code_string, "utf-8")
        tree = self.parser.parse(code_bytes)
        root = tree.root_node

        file_name = os.path.basename(file_path)
        
        # We'll normalize the path to be relative or absolute consistently
        normalized_path = os.path.abspath(file_path)

        file_data = {
            "path": normalized_path,
            "name": file_name,
            "content": code_string
        }

        classes = []
        functions = []

        for child in root.children:
            if child.type == 'class_definition':
                class_name = child.child_by_field_name('name').text.decode('utf-8')
                doc = self._get_docstring(child)
                start = child.start_point.row + 1
                end = child.end_point.row + 1
                code = child.text.decode('utf-8')
                class_id = f"{normalized_path}::{class_name}"

                methods = []
                body_node = child.child_by_field_name('body')
                if body_node:
                    for sub_child in body_node.children:
                        if sub_child.type == 'function_definition':
                            method_name = sub_child.child_by_field_name('name').text.decode('utf-8')
                            m_doc = self._get_docstring(sub_child)
                            m_start = sub_child.start_point.row + 1
                            m_end = sub_child.end_point.row + 1
                            m_code = sub_child.text.decode('utf-8')
                            method_id = f"{normalized_path}::{class_name}::{method_name}"

                            m_calls = []
                            self._find_calls(sub_child, m_calls)

                            methods.append({
                                "id": method_id,
                                "name": method_name,
                                "docstring": m_doc,
                                "start_line": m_start,
                                "end_line": m_end,
                                "code": m_code,
                                "calls": m_calls
                            })

                classes.append({
                    "id": class_id,
                    "name": class_name,
                    "docstring": doc,
                    "start_line": start,
                    "end_line": end,
                    "code": code,
                    "methods": methods
                })

            elif child.type == 'function_definition':
                func_name = child.child_by_field_name('name').text.decode('utf-8')
                doc = self._get_docstring(child)
                start = child.start_point.row + 1
                end = child.end_point.row + 1
                code = child.text.decode('utf-8')
                func_id = f"{normalized_path}::{func_name}"

                calls = []
                self._find_calls(child, calls)

                functions.append({
                    "id": func_id,
                    "name": func_name,
                    "docstring": doc,
                    "start_line": start,
                    "end_line": end,
                    "code": code,
                    "calls": calls
                })

        return {
            "file": file_data,
            "classes": classes,
            "functions": functions
        }