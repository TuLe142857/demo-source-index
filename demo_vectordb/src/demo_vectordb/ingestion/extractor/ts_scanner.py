import os
import tree_sitter
import tree_sitter_python
from typing import List, Dict, Any

class TreeSitterScanner:
    """
    A scanner that parses a Python file using tree-sitter, executes a query to locate
    all function or variable call sites, and collects their names and coordinates.
    """
    def __init__(self):
        self.language = tree_sitter.Language(tree_sitter_python.language())
        self.parser = tree_sitter.Parser(self.language)
        # Tree-sitter query to match call expressions (identifiers or attribute nodes)
        self.query_str = """
        (call
          function: [
              (identifier) @name
              (attribute
                attribute: (identifier) @name)
          ])
        """
        self.query = tree_sitter.Query(self.language, self.query_str)

    def scan_file(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Scans a Python source file and returns a list of dictionaries, each describing a call site:
        {
            "file_path": str,
            "file_uri": str,
            "callee_name": str,
            "line": int,      # 0-based row index
            "column": int     # 0-based column index
        }
        """
        abs_path = os.path.abspath(file_path)
        normalized_path = abs_path.replace(os.sep, '/')
        if not normalized_path.startswith('/'):
            file_uri = f"file:///{normalized_path}"
        else:
            file_uri = f"file://{normalized_path}"

        if not os.path.exists(abs_path):
            raise FileNotFoundError(f"File not found: {abs_path}")

        with open(abs_path, 'rb') as f:
            content = f.read()

        tree = self.parser.parse(content)
        cursor = tree_sitter.QueryCursor(self.query)
        matches = cursor.matches(tree.root_node)

        calls = []
        for _, capture_dict in matches:
            if 'name' in capture_dict:
                for name_node in capture_dict['name']:
                    callee_name = name_node.text.decode('utf-8')
                    start_pt = name_node.start_point
                    calls.append({
                        "file_path": abs_path,
                        "file_uri": file_uri,
                        "callee_name": callee_name,
                        "line": start_pt.row,
                        "column": start_pt.column
                    })
        return calls
