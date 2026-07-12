from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "password"

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

def test_connection():
    with driver.session() as session:
        result = session.run("RETURN 'Connected to Neo4j!' AS message")
        print(result.single()["message"])

if __name__ == "__main__":
    try:
        test_connection()
    finally:
        driver.close()