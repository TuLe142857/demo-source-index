import ast
import sys
from pathlib import Path

# Add src folder to sys.path to allow imports of demo_neo4j
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from demo_neo4j.graph.driver import driver
from demo_neo4j.models.graph_types import NodeType, EdgeType

class PythonASTExtractor(ast.NodeVisitor):
    def __init__(self, file_path: Path, project_name: str):
        self.file_path = file_path
        self.file_name = file_path.name
        self.project_name = project_name
        
        # Unique identifier of file
        self.file_qn = f"input_src/{self.file_name}"
        
        self.nodes = []
        self.edges = []
        
        self.current_class = None
        self.current_class_qn = None
        self.current_function = None
        self.current_function_qn = None
        
        # Create File node
        self.nodes.append({
            "label": NodeType.FILE.value,
            "qualified_name": self.file_qn,
            "name": self.file_name,
            "file_path": str(self.file_path),
            "start_line": 1,
            "end_line": 100,  # Estimated
            "properties": {}
        })

    def extract(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Update file node end line
        lines = content.splitlines()
        self.nodes[0]["end_line"] = len(lines)
        
        tree = ast.parse(content)
        self.visit(tree)
        return self.nodes, self.edges

    def visit_Import(self, node):
        for alias in node.names:
            # For simplicity, map to target file if it exists in input_src
            target_file_qn = f"input_src/{alias.name}.py"
            self.edges.append({
                "source_qn": self.file_qn,
                "target_qn": target_file_qn,
                "type": EdgeType.IMPORTS.value,
                "properties": {"line": node.lineno}
            })
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        module = node.module or ""
        target_file_qn = f"input_src/{module}.py"
        # Edge from this file to the imported module
        self.edges.append({
            "source_qn": self.file_qn,
            "target_qn": target_file_qn,
            "type": EdgeType.IMPORTS.value,
            "properties": {"line": node.lineno, "imported_symbols": [alias.name for alias in node.names]}
        })
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        class_qn = f"{self.file_qn}::{node.name}"
        
        # Create Class node
        self.nodes.append({
            "label": NodeType.CLASS.value,
            "qualified_name": class_qn,
            "name": node.name,
            "file_path": str(self.file_path),
            "start_line": node.lineno,
            "end_line": node.end_lineno,
            "properties": {}
        })
        
        # File CONTAINS Class
        self.edges.append({
            "source_qn": self.file_qn,
            "target_qn": class_qn,
            "type": EdgeType.CONTAINS.value,
            "properties": {}
        })
        
        # Class inherits from bases
        for base in node.bases:
            if isinstance(base, ast.Name):
                # Target class QN (simplification: assume it's in the same project/file or imported)
                # We'll resolve the base QN dynamically or link by name
                # For our demo, "Animal" is in animal.py
                base_name = base.id
                base_qn = f"input_src/animal.py::{base_name}"
                self.edges.append({
                    "source_qn": class_qn,
                    "target_qn": base_qn,
                    "type": EdgeType.INHERITS.value,
                    "properties": {}
                })
        
        old_class = self.current_class
        old_class_qn = self.current_class_qn
        self.current_class = node.name
        self.current_class_qn = class_qn
        
        self.generic_visit(node)
        
        self.current_class = old_class
        self.current_class_qn = old_class_qn

    def visit_FunctionDef(self, node):
        is_method = self.current_class is not None
        
        if is_method:
            func_qn = f"{self.current_class_qn}.{node.name}"
            label = NodeType.METHOD.value
        else:
            func_qn = f"{self.file_qn}::{node.name}"
            label = NodeType.FUNCTION.value
            
        # Create Function/Method node
        self.nodes.append({
            "label": label,
            "qualified_name": func_qn,
            "name": node.name,
            "file_path": str(self.file_path),
            "start_line": node.lineno,
            "end_line": node.end_lineno,
            "properties": {"is_method": is_method}
        })
        
        # Owner CONTAINS function/method
        owner_qn = self.current_class_qn if is_method else self.file_qn
        self.edges.append({
            "source_qn": owner_qn,
            "target_qn": func_qn,
            "type": EdgeType.CONTAINS.value,
            "properties": {}
        })
        
        old_func = self.current_function
        old_func_qn = self.current_function_qn
        self.current_function = node.name
        self.current_function_qn = func_qn
        
        self.generic_visit(node)
        
        self.current_function = old_func
        self.current_function_qn = old_func_qn

    def visit_Call(self, node):
        callee_name = None
        if isinstance(node.func, ast.Name):
            callee_name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            callee_name = node.func.attr
            
        # If call is made inside a function/method
        if callee_name and self.current_function_qn:
            self.edges.append({
                "source_qn": self.current_function_qn,
                "target_name": callee_name, # Store name first, resolve to QN later
                "type": EdgeType.CALLS.value,
                "properties": {"line": node.lineno}
            })
        self.generic_visit(node)

def clear_db():
    print("Clearing existing data in Neo4j...")
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")

def ingest_to_neo4j(nodes, edges):
    print("Ingesting nodes into Neo4j...")
    with driver.session() as session:
        for node in nodes:
            # Dynamic label query (safe because we control NodeType values)
            query = f"""
            MERGE (n:{node['label']} {{project: $project, qualifiedName: $qualified_name}})
            SET n.name = $name, n.filePath = $file_path, 
                n.startLine = $start_line, n.endLine = $end_line
            SET n += $properties
            """
            session.run(query, 
                        project="demo-neo4j",
                        qualified_name=node["qualified_name"],
                        name=node["name"],
                        file_path=node["file_path"],
                        start_line=node["start_line"],
                        end_line=node["end_line"],
                        properties=node["properties"])
            print(f"  Merged Node: [{node['label']}] {node['qualified_name']}")
            
        print("Ingesting edges into Neo4j...")
        for edge in edges:
            query = f"""
            MATCH (src {{qualifiedName: $source_qn}}), (tgt {{qualifiedName: $target_qn}})
            MERGE (src)-[r:{edge['type']}]->(tgt)
            SET r += $properties
            """
            result = session.run(query, 
                                 source_qn=edge["source_qn"],
                                 target_qn=edge["target_qn"],
                                 properties=edge["properties"])
            print(f"  Merged Edge: ({edge['source_qn']}) -[:{edge['type']}]-> ({edge['target_qn']})")

def main():
    project_root = Path(__file__).resolve().parents[2]
    input_dir = project_root / "input_src"
    
    if not input_dir.exists():
        print(f"Error: Input directory {input_dir} does not exist.")
        return
        
    print(f"Scanning Python files in {input_dir}...")
    py_files = list(input_dir.glob("*.py"))
    
    all_nodes = []
    all_edges = []
    
    # Phase 1: Parse AST and extract Nodes and Edges
    for py_file in py_files:
        print(f"Parsing: {py_file.name}")
        extractor = PythonASTExtractor(py_file, "demo-neo4j")
        nodes, edges = extractor.extract()
        all_nodes.extend(nodes)
        all_edges.extend(edges)
        
    # Phase 2: Resolve Call QNs
    # Map from simple function/class/method name to its qualified name
    name_to_qn = {}
    for node in all_nodes:
        # Map class, function, and method names
        if node["label"] in [NodeType.CLASS.value, NodeType.FUNCTION.value, NodeType.METHOD.value]:
            name_to_qn[node["name"]] = node["qualified_name"]
            
    # Also handle method calls by checking if target_name is in name_to_qn
    resolved_edges = []
    for edge in all_edges:
        if "target_qn" in edge:
            resolved_edges.append(edge)
        elif "target_name" in edge:
            target_name = edge["target_name"]
            # Resolve callee name to QN
            if target_name in name_to_qn:
                edge["target_qn"] = name_to_qn[target_name]
                del edge["target_name"]
                resolved_edges.append(edge)
            else:
                # If target is not found in defined symbols (e.g. print, builtins), skip or log
                # For this demo, let's just log and skip
                # print(f"  Skipped call to builtin/external: {target_name}")
                pass

    # Phase 3: DB Operations
    clear_db()
    ingest_to_neo4j(all_nodes, resolved_edges)
    print("Ingestion complete!")

if __name__ == "__main__":
    main()
