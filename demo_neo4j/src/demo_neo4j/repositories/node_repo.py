import dataclasses
from typing import List, Optional
from demo_neo4j.models.graph_types import NodeType, Node

class NodeRepository:
    def __init__(self, driver):
        self.driver = driver

    def search_node(self, node_type: NodeType, node_name: str) -> Optional[dict]:
        cypher = f"""
        MATCH (n:{node_type.value})
        WHERE n.name = $node_name
        RETURN n
        LIMIT 1
        """

        with self.driver.session() as session:
            result = session.run(cypher, node_name=node_name)
            record = result.single()

            if record is None:
                return None

            return dict(record["n"])
        
    def trace_call_path(self):
        pass

    def run_query(self, query: str):
        with self.driver.session() as session:
            result = session.run(query)
            records = result.data()

            records = [dict(record) for record in list(records)]

            return records
        
    def batch_upsert(self, nodes: List[Node], batch_size: int = 1000):
        """
        Sử dụng UNWIND để insert an toàn hàng ngàn Node, 
        có chia lô (chunking) và tự động retry.
        """
        query = """
        UNWIND $batch AS data
        MERGE (n:CodeNode {project: data.project, qualifiedName: data.qualified_name})
        ON CREATE SET n.name = data.name, n.filePath = data.file_path, 
                      n.startLine = data.start_line, n.endLine = data.end_line, 
                      n.properties = data.propertiess
        ON MATCH SET n.name = data.name, n.filePath = data.file_path, 
                     n.startLine = data.start_line, n.endLine =s data.end_line, 
                     n.properties = data.properties
        WITH n, data
        CALL apoc.create.addLabels(n, [data.label]) YIELD node
        RETURN count(node) AS updated_count
        """
        
        # Hàm nội bộ để chạy transaction cho 1 chunk
        def _execute_chunk(tx, chunk_data):
            result = tx.run(query, batch=chunk_data)
            # Lấy số lượng node đã update trong chunk này
            return result.single()["updated_count"] 

        total_updated = 0
        
        # Mở session và bắt đầu chia lô để xử lý
        with self.driver.session() as session:
            for i in range(0, len(nodes), batch_size):
                # 1. Cắt lấy một lô (chunk)
                chunk_nodes = nodes[i : i + batch_size]
                
                # 2. Chuyển đổi an toàn Dataclass -> Dict
                chunk_data = [dataclasses.asdict(node) for node in chunk_nodes]
                
                # 3. Ghi dữ liệu với execute_write (tự động retry nếu lỗi mạng)
                updated_in_chunk = session.execute_write(_execute_chunk, chunk_data)
                total_updated += updated_in_chunk

        return total_updated