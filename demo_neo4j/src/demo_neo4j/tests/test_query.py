from demo_neo4j.graph.driver import driver
from demo_neo4j.services.query import QueryService
from demo_neo4j.models.graph_types import NodeType

who_call_this = """
    MATC
"""

if __name__ == "__main__":
    query_service = QueryService(driver=driver)

    #result = query_service.search_graph(node_type=NodeType.FUNCTION, node_name="create_dog")

    all_method = query_service.execute_query(query=f"MATCH (n: {NodeType.METHOD.value}) RETURN n")



    for method in all_method:
        print(method["n"]["name"])
        print(method["n"]["qualifiedName"])