import os
import sys
import argparse
import json
import re
from llama_cpp import Llama
from demo_graphdb.db.driver import Neo4jDriver
from demo_graphdb.db.session import execute
from demo_graphdb.ingest_data.parser import PythonParser
from demo_graphdb.ingest_data.ingestor import CodeIngestor

# Reconfigure stdout to support Vietnamese character displays on Windows
sys.stdout.reconfigure(encoding='utf-8')

class GraphRAGApp:
    def __init__(self, model_path: str, db_uri: str, db_user: str, db_pass: str):
        self.model_path = model_path
        self.db_uri = db_uri
        self.db_user = db_user
        self.db_pass = db_pass
        self.llm = None
        self.parser = PythonParser()
        self.ingestor = CodeIngestor()

    def connect_db(self):
        try:
            Neo4jDriver.connect(self.db_uri, self.db_user, self.db_pass)
            # Verify connectivity
            driver = Neo4jDriver.driver()
            driver.verify_connectivity()
        except Exception as e:
            print(f"[-] Lỗi kết nối Neo4j: {e}")
            print("[*] Hãy chắc chắn rằng container Docker Neo4j đang chạy.")
            sys.exit(1)

    def load_llm(self):
        if self.llm is None:
            print("[+] Đang tải mô hình Phi-4 GGUF (vui lòng chờ)...")
            try:
                self.llm = Llama(
                    model_path=self.model_path,
                    n_ctx=2048,
                    verbose=False
                )
                print("[+] Tải mô hình thành công!")
            except Exception as e:
                print(f"[-] Không thể tải mô hình Phi-4 từ: {self.model_path}")
                print(f"[-] Lỗi chi tiết: {e}")
                sys.exit(1)

    def _generate_response(self, system_prompt: str, user_prompt: str, max_tokens: int = 1000) -> str:
        # ChatML format for Phi-4
        prompt = f"<|im_start|>system\n{system_prompt}<|im_end|>\n<|im_start|>user\n{user_prompt}<|im_end|>\n<|im_start|>assistant\n"
        response = self.llm(
            prompt,
            max_tokens=max_tokens,
            temperature=0.1,
            stop=["<|im_end|>", "<|im_start|>"]
        )
        return response["choices"][0]["text"].strip()

    def _clean_json_output(self, text: str) -> dict:
        # Strip markdown syntax formatting
        cleaned = re.sub(r"```json\s*", "", text, flags=re.IGNORECASE)
        cleaned = re.sub(r"```\s*", "", cleaned)
        cleaned = cleaned.strip()
        try:
            return json.loads(cleaned)
        except Exception:
            # Fallback regex parsing to extract words
            words = re.findall(r"\b\w{3,}\b", text)
            return {"functions": words, "classes": [], "files": [], "keywords": words}

    def analyze_query_intent(self, query: str) -> dict:
        print("[*] Đang phân tích intent câu hỏi...")
        system_prompt = (
            "You are an expert assistant that extracts code search criteria from user queries.\n"
            "Analyze the query and identify target function names, class names, file names, or general keywords.\n"
            "Output your analysis ONLY as a valid JSON object with keys 'functions', 'classes', 'files', and 'keywords'.\n"
            "Do not output markdown code blocks (e.g. ```json), introductory text, or concluding text."
        )
        raw_output = self._generate_response(system_prompt, query, max_tokens=256)
        intent = self._clean_json_output(raw_output)
        print(f"[+] Intent đã trích xuất: {intent}")
        return intent

    def retrieve_code_context(self, intent: dict) -> str:
        contexts = []
        retrieved_nodes = set()

        # Retrieve functions
        for func_name in intent.get("functions", []):
            results = execute(
                """
                MATCH (fn:Function)
                WHERE fn.name = $name OR fn.name CONTAINS $name
                RETURN fn.id AS id, fn.name AS name, fn.code AS code, fn.docstring AS docstring, fn.is_method AS is_method
                """,
                name=func_name
            )
            for r in results:
                if r["id"] not in retrieved_nodes:
                    retrieved_nodes.add(r["id"])
                    node_type = "Method" if r["is_method"] else "Function"
                    contexts.append(
                        f"--- Node ({node_type}): {r['name']} ---\n"
                        f"Docstring: {r['docstring']}\n"
                        f"Code:\n{r['code']}\n"
                    )
                    
                    # Fetch callers (1-hop traversal)
                    callers = execute(
                        """
                        MATCH (caller:Function)-[:CALLS]->(fn:Function {id: $id})
                        RETURN caller.name AS name
                        """,
                        id=r["id"]
                    )
                    if callers:
                        caller_names = ", ".join([c["name"] for c in callers])
                        contexts.append(f"Note: This {node_type.lower()} is called by functions: {caller_names}\n")

                    # Fetch callees (1-hop traversal)
                    callees = execute(
                        """
                        MATCH (fn:Function {id: $id})-[:CALLS]->(callee:Function)
                        RETURN callee.name AS name
                        """,
                        id=r["id"]
                    )
                    if callees:
                        callee_names = ", ".join([c["name"] for c in callees])
                        contexts.append(f"Note: This {node_type.lower()} calls functions: {callee_names}\n")

        # Retrieve classes
        for class_name in intent.get("classes", []):
            results = execute(
                """
                MATCH (c:Class)
                WHERE c.name = $name OR c.name CONTAINS $name
                RETURN c.id AS id, c.name AS name, c.code AS code, c.docstring AS docstring
                """,
                name=class_name
            )
            for r in results:
                if r["id"] not in retrieved_nodes:
                    retrieved_nodes.add(r["id"])
                    contexts.append(
                        f"--- Node (Class): {r['name']} ---\n"
                        f"Docstring: {r['docstring']}\n"
                        f"Code:\n{r['code']}\n"
                    )

        # Retrieve files
        for file_name in intent.get("files", []):
            results = execute(
                """
                MATCH (f:File)
                WHERE f.name = $name OR f.name CONTAINS $name
                RETURN f.path AS id, f.name AS name, f.content AS code
                """,
                name=file_name
            )
            for r in results:
                if r["id"] not in retrieved_nodes:
                    retrieved_nodes.add(r["id"])
                    contexts.append(
                        f"--- Node (File): {r['name']} ---\n"
                        f"Code:\n{r['code']}\n"
                    )

        # Fallback keyword search
        if not contexts:
            for keyword in intent.get("keywords", []):
                if not keyword or len(keyword) < 3:
                    continue
                results = execute(
                    """
                    MATCH (node)
                    WHERE (node:Function OR node:Class OR node:File) AND (
                        node.name CONTAINS $kw OR
                        (node.docstring IS NOT NULL AND node.docstring CONTAINS $kw) OR
                        (node.code IS NOT NULL AND node.code CONTAINS $kw) OR
                        (node.content IS NOT NULL AND node.content CONTAINS $kw)
                    )
                    RETURN labels(node)[0] AS type, node.id AS id, node.name AS name, 
                           coalesce(node.code, node.content) AS code, node.docstring AS docstring
                    """,
                    kw=keyword
                )
                for r in results:
                    node_id = r["id"] if r["id"] else r["name"]
                    if node_id not in retrieved_nodes:
                        retrieved_nodes.add(node_id)
                        contexts.append(
                            f"--- Node ({r['type']}): {r['name']} ---\n"
                            f"Docstring: {r.get('docstring') or 'N/A'}\n"
                            f"Code:\n{r['code']}\n"
                        )

        return "\n".join(contexts) if contexts else "Không tìm thấy code snippet liên quan trong cơ sở dữ liệu."

    def answer_query(self, query: str):
        self.load_llm()
        
        # 1. Analyze intent
        intent = self.analyze_query_intent(query)
        
        # 2. Retrieve code blocks from Neo4j
        code_context = self.retrieve_code_context(intent)
        print("\n=== DỮ LIỆU TRUY VẤN ĐƯỢC TỪ NEO4J ===")
        print(code_context[:500] + ("..." if len(code_context) > 500 else ""))
        print("======================================\n")

        # 3. Generate final answer
        print("[*] Đang tổng hợp câu trả lời...")
        system_prompt = (
            "You are a helpful software development assistant.\n"
            "Below is the relevant source code retrieved from the knowledge graph:\n\n"
            f"{code_context}\n\n"
            "Use ONLY the code context provided above to answer the user query.\n"
            "Write the explanation in Vietnamese. Be concise, clear, and refer to specific function or class names."
        )
        
        answer = self._generate_response(system_prompt, query, max_tokens=1500)
        print("\n=== PHẢN HỒI TỪ PHI-4 RAG ===")
        print(answer)
        print("============================\n")

    def ingest_path(self, target_path: str):
        print(f"[*] Bắt đầu quét và parse đường dẫn: {target_path}")
        if os.path.isfile(target_path):
            if target_path.endswith(".py"):
                parsed = self.parser.parse_file(target_path)
                if parsed:
                    self.ingestor.ingest_file_data(parsed)
            else:
                print("[-] Chỉ hỗ trợ file Python (.py).")
        elif os.path.isdir(target_path):
            for root, _, files in os.walk(target_path):
                for file in files:
                    if file.endswith(".py"):
                        full_path = os.path.join(root, file)
                        parsed = self.parser.parse_file(full_path)
                        if parsed:
                            self.ingestor.ingest_file_data(parsed)
        else:
            print("[-] Đường dẫn không tồn tại.")

def main():
    parser = argparse.ArgumentParser(description="GraphRAG CLI tool using Neo4j & Phi-4")
    parser.add_argument("action", choices=["ingest", "query", "chat"], help="Hành động cần thực hiện")
    parser.add_argument("param", nargs="?", help="Đường dẫn file/thư mục để ingest, hoặc nội dung câu hỏi")
    
    # Custom config options
    parser.add_argument("--model-path", default=r"c:\Hieu\Project\demo-source-index\demo-graphdb\src\Phi-4-mini-instruct-Q4_K_M.gguf", help="Đường dẫn file GGUF Phi-4")
    parser.add_argument("--db-uri", default="bolt://localhost:7687", help="Neo4j bolt URI")
    parser.add_argument("--db-user", default="neo4j", help="Neo4j username")
    parser.add_argument("--db-pass", default="password123", help="Neo4j password")

    args = parser.parse_args()

    app = GraphRAGApp(args.model_path, args.db_uri, args.db_user, args.db_pass)
    app.connect_db()

    if args.action == "ingest":
        if not args.param:
            print("[-] Lỗi: Cần cung cấp đường dẫn file hoặc thư mục để ingest.")
            sys.exit(1)
        app.ingest_path(args.param)
    
    elif args.action == "query":
        if not args.param:
            print("[-] Lỗi: Cần cung cấp nội dung câu hỏi.")
            sys.exit(1)
        app.answer_query(args.param)
        
    elif args.action == "chat":
        print("\n=== Đang vào chế độ Chat tương tác (nhập 'exit' hoặc 'quit' để thoát) ===")
        app.load_llm()
        while True:
            try:
                query = input("User >> ").strip()
                if not query:
                    continue
                if query.lower() in ["exit", "quit"]:
                    break
                app.answer_query(query)
            except KeyboardInterrupt:
                print("\nThoát...")
                break

    # Clean up DB driver connection
    Neo4jDriver.close()

if __name__ == "__main__":
    main()
