import os
import sys
from tabulate import tabulate

# Add src directory to path so we can import demo_vectordb
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from demo_vectordb.ingestion.extractor.pipeline import CoordinationPipeline

def main():
    db_path = "calls.db"
    
    # Clean up old database file
    if os.path.exists(db_path):
        try:
            os.remove(db_path)
            print(f"Removed existing database file: {db_path}")
        except Exception as e:
            print(f"Could not remove old database: {e}")

    # Determine files to scan
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sample_dir = os.path.join(current_dir, "sample_code")
    files_to_scan = [
        os.path.join(sample_dir, "helper.py"),
        os.path.join(sample_dir, "main.py")
    ]
    
    # Setup and run coordination pipeline
    pipeline = CoordinationPipeline(project_root=sample_dir, db_path=db_path)
    
    print("\n================== RUNNING PIPELINE ==================")
    pipeline.run(files_to_scan)
    print("======================================================\n")

    # Fetch and print database results
    print("================ DATABASE CALL GRAPH EDGES ================")
    edges = pipeline.db.get_all_edges()
    
    if not edges:
        print("No edges found in the SQLite database.")
        return

    # Helper function to get relative paths or base names for readability
    def format_path(path_uri):
        if not path_uri:
            return "N/A"
        # Extract path from file URI
        if path_uri.startswith("file:///"):
            path = path_uri[8:]
        elif path_uri.startswith("file://"):
            path = path_uri[7:]
        else:
            path = path_uri
        return os.path.basename(path)

    table_data = []
    for edge in edges:
        src_file = format_path(edge["source_file"])
        src_pos = f"L{edge['source_line']} C{edge['source_col']}"
        callee = edge["callee_name"]
        
        tgt_file = format_path(edge["target_file"])
        tgt_pos = f"L{edge['target_line']} C{edge['target_col']}" if edge["target_line"] is not None else "N/A"
        
        table_data.append([
            edge["id"],
            src_file,
            src_pos,
            callee,
            tgt_file,
            tgt_pos,
            edge["edge_type"]
        ])

    headers = ["ID", "Source File", "Source Coord", "Callee", "Target File", "Target Coord", "Edge Type"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    print("==========================================================\n")

if __name__ == "__main__":
    main()
