import os
from demo_graphdb.db.driver import Neo4jDriver
from demo_graphdb.db.session import execute

class CodeIngestor:
    def __init__(self):
        pass

    def ingest_file_data(self, parsed_data):
        """
        Ingests the parsed python file data into Neo4j.
        parsed_data is the dictionary returned by PythonParser.parse_file.
        """
        if not parsed_data:
            print("[-] Không có dữ liệu để ingest.")
            return False

        file_info = parsed_data["file"]
        classes = parsed_data["classes"]
        functions = parsed_data["functions"]

        print(f"[+] Đang ingest file: {file_info['name']}...")

        # 1. Ingest File Node
        execute(
            """
            MERGE (f:File {path: $path})
            SET f.name = $name, f.content = $content
            """,
            path=file_info["path"],
            name=file_info["name"],
            content=file_info["content"]
        )

        # 2. Ingest Classes
        for cls in classes:
            execute(
                """
                MERGE (c:Class {id: $id})
                SET c.name = $name,
                    c.docstring = $docstring,
                    c.start_line = $start_line,
                    c.end_line = $end_line,
                    c.code = $code
                """,
                id=cls["id"],
                name=cls["name"],
                docstring=cls["docstring"],
                start_line=cls["start_line"],
                end_line=cls["end_line"],
                code=cls["code"]
            )

            # Link File -> Class
            execute(
                """
                MATCH (f:File {path: $file_path})
                MATCH (c:Class {id: $class_id})
                MERGE (f)-[:CONTAINS]->(c)
                """,
                file_path=file_info["path"],
                class_id=cls["id"]
            )

            # Ingest Methods inside Class
            for method in cls["methods"]:
                execute(
                    """
                    MERGE (m:Function {id: $id})
                    SET m.name = $name,
                        m.docstring = $docstring,
                        m.start_line = $start_line,
                        m.end_line = $end_line,
                        m.code = $code,
                        m.is_method = true
                    """,
                    id=method["id"],
                    name=method["name"],
                    docstring=method["docstring"],
                    start_line=method["start_line"],
                    end_line=method["end_line"],
                    code=method["code"]
                )

                # Link Class -> Method
                execute(
                    """
                    MATCH (c:Class {id: $class_id})
                    MATCH (m:Function {id: $method_id})
                    MERGE (c)-[:CONTAINS]->(m)
                    """,
                    class_id=cls["id"],
                    method_id=method["id"]
                )

        # 3. Ingest Top-level Functions
        for func in functions:
            execute(
                """
                MERGE (f:Function {id: $id})
                SET f.name = $name,
                    f.docstring = $docstring,
                    f.start_line = $start_line,
                    f.end_line = $end_line,
                    f.code = $code,
                    f.is_method = false
                """,
                id=func["id"],
                name=func["name"],
                docstring=func["docstring"],
                start_line=func["start_line"],
                end_line=func["end_line"],
                code=func["code"]
            )

            # Link File -> Function
            execute(
                """
                MATCH (file:File {path: $file_path})
                MATCH (func:Function {id: $func_id})
                MERGE (file)-[:CONTAINS]->(func)
                """,
                file_path=file_info["path"],
                func_id=func["id"]
            )

        # 4. Establish CALLS relationships
        # We perform call linking after all nodes are inserted to ensure targets exist
        print("[+] Đang tạo các liên kết CALLS...")

        # For methods
        for cls in classes:
            for method in cls["methods"]:
                for called_name in method["calls"]:
                    # Skip standard/builtin names to keep graph clean
                    if called_name in ["print", "len", "range", "set", "list", "dict", "str", "int", "append", "pop", "split", "strip", "join"]:
                        continue
                    execute(
                        """
                        MATCH (caller:Function {id: $caller_id})
                        MATCH (callee:Function {name: $callee_name})
                        MERGE (caller)-[:CALLS]->(callee)
                        """,
                        caller_id=method["id"],
                        callee_name=called_name
                    )

        # For top-level functions
        for func in functions:
            for called_name in func["calls"]:
                if called_name in ["print", "len", "range", "set", "list", "dict", "str", "int", "append", "pop", "split", "strip", "join"]:
                    continue
                execute(
                    """
                    MATCH (caller:Function {id: $caller_id})
                    MATCH (callee:Function {name: $callee_name})
                    MERGE (caller)-[:CALLS]->(callee)
                    """,
                    caller_id=func["id"],
                    callee_name=called_name
                )

        print("[+] Ingest thành công!")
        return True
