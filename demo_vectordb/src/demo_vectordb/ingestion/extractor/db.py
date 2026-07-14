import sqlite3
from typing import List, Dict, Any, Optional

class CallGraphDB:
    """
    Manages SQLite database storage for CALLS relationships, which link
    the source position of a function call to the target definition resolved by the LSP.
    """
    def __init__(self, db_path: str = "calls.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS calls_edges (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    source_file TEXT NOT NULL,
                    source_line INTEGER NOT NULL,
                    source_col INTEGER NOT NULL,
                    callee_name TEXT NOT NULL,
                    target_file TEXT,
                    target_line INTEGER,
                    target_col INTEGER,
                    edge_type TEXT NOT NULL DEFAULT 'CALLS'
                )
            """)
            conn.commit()

    def insert_call_edge(self, 
                         source_file: str, 
                         source_line: int, 
                         source_col: int, 
                         callee_name: str, 
                         target_file: Optional[str], 
                         target_line: Optional[int], 
                         target_col: Optional[int]):
        """Inserts a CALLS edge entry connecting the caller site to the callee definition site."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO calls_edges 
                (source_file, source_line, source_col, callee_name, target_file, target_line, target_col, edge_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, 'CALLS')
            """, (source_file, source_line, source_col, callee_name, target_file, target_line, target_col))
            conn.commit()

    def get_all_edges(self) -> List[Dict[str, Any]]:
        """Retrieves all call edges stored in the SQLite database."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM calls_edges")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    def clear_db(self):
        """Drops and recreates the calls_edges table."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS calls_edges")
            conn.commit()
        self._init_db()
