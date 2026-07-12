import sys
from pathlib import Path

# Add src folder to sys.path to allow imports of demo_neo4j
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from demo_neo4j.graph.driver import driver

def run_query(title, cypher_query):
    print("=" * 60)
    print(f"QUERY: {title}")
    print("-" * 60)
    print(f"Cypher:\n{cypher_query.strip()}\n")
    print("Results:")
    
    with driver.session() as session:
        result = session.run(cypher_query)
        records = list(result)
        if not records:
            print("  No records found.")
        else:
            # Dynamically determine columns from the keys
            keys = result.keys()
            header = " | ".join(f"{k:<25}" for k in keys)
            print(header)
            print("-" * len(header))
            for record in records:
                row = " | ".join(f"{str(record[k]):<25}" for k in keys)
                print(row)
    print("=" * 60 + "\n")

def main():
    print("--- STARTING CYPHER QUERIES TEST ON NEO4J ---\n")
    
    # 1. List all code nodes
    run_query(
        "List all parsed code nodes",
        """
        MATCH (n)
        RETURN labels(n)[0] AS Label, n.name AS Name, n.qualifiedName AS QualifiedName
        ORDER BY Label, Name
        """
    )
    
    # 2. List inheritance relationships
    run_query(
        "Classes and Inheritance",
        """
        MATCH (child:Class)-[:INHERITS]->(parent:Class)
        RETURN child.name AS ChildClass, parent.name AS ParentClass
        """
    )
    
    # 3. List contains relationships
    run_query(
        "What code elements are defined inside which file/class?",
        """
        MATCH (container)-[:CONTAINS]->(contained)
        RETURN labels(container)[0] AS ContainerType, container.name AS ContainerName,
               labels(contained)[0] AS ContainedType, contained.name AS ContainedName
        ORDER BY ContainerType, ContainerName
        """
    )
    
    # 4. List imports relationships
    run_query(
        "File level Import dependencies",
        """
        MATCH (f:File)-[r:IMPORTS]->(imported:File)
        RETURN f.name AS File, imported.name AS ImportedFile, r.imported_symbols AS ImportedSymbols
        """
    )
    
    # 5. List function calls
    run_query(
        "Function/Method calls",
        """
        MATCH (caller)-[r:CALLS]->(callee)
        RETURN labels(caller)[0] AS CallerType, caller.name AS CallerName,
               labels(callee)[0] AS CalleeType, callee.name AS CalleeName,
               r.line AS LineNumber
        """
    )

if __name__ == "__main__":
    try:
        main()
    finally:
        driver.close()
