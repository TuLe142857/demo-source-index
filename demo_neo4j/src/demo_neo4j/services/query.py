from demo_neo4j.repositories.node_repo import NodeRepository
from demo_neo4j.models.graph_types import NodeType

class QueryService:
    def __init__(self, driver):
        self.node_repo = NodeRepository(driver)

    def search_graph(self, node_type: NodeType, node_name: str):
        """
        Tool: search_graph (Symbol search)
        Tìm kiếm các Node trong đồ thị dựa trên tên và loại.
        """
        # Gọi trực tiếp logic từ tầng Repository
        results = self.node_repo.search_node(
            node_type=node_type, 
            node_name=node_name
        )
        
        return results
    
    def execute_query(self, query: str):
        results = self.node_repo.run_query(query=query)
        return results