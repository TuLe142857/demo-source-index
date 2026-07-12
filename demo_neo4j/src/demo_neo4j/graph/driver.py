from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    "bolt://localhost:7687", # Phương thức bolt nhanh hơn http
    auth=("neo4j", "password"),
)