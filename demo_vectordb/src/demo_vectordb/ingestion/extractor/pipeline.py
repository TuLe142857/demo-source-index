import sys
import os
import time
from typing import List, Optional, Tuple
from .lsp_client import LSPClient
from .ts_scanner import TreeSitterScanner
from .db import CallGraphDB

class CoordinationPipeline:
    """
    Coordinates the process:
    1. Parse files with Tree-sitter to find call site coordinates.
    2. Start Python LSP Server (jedi-language-server) in the background.
    3. Notify LSP of open files and query it for the target definition of each call site.
    4. Save caller coordinates, callee name, and resolved target definition coordinates into SQLite.
    5. Shut down LSP server gracefully.
    """
    def __init__(self, project_root: str, db_path: str = "calls.db"):
        self.project_root = os.path.abspath(project_root)
        self.db = CallGraphDB(db_path)
        self.scanner = TreeSitterScanner()
        # Resolve path to jedi-language-server in the virtual environment
        binary_name = "jedi-language-server.exe" if sys.platform == "win32" else "jedi-language-server"
        bin_dir = "Scripts" if sys.platform == "win32" else "bin"
        lsp_bin = os.path.join(sys.prefix, bin_dir, binary_name)
        if not os.path.exists(lsp_bin):
            lsp_bin = binary_name  # Fallback to system PATH
        self.server_cmd = [lsp_bin]
        self.lsp_client = LSPClient(self.server_cmd, self.project_root)

    def run(self, files: List[str]):
        """Runs the coordination pipeline on a set of target Python source files."""
        print("[Pipeline] Scanning files using Tree-sitter...")
        all_calls = []
        for file in files:
            abs_file = os.path.abspath(file)
            print(f"  Scanning: {abs_file}")
            file_calls = self.scanner.scan_file(abs_file)
            all_calls.extend(file_calls)

        print(f"[Pipeline] Found {len(all_calls)} calls with Tree-sitter.")

        print("[Pipeline] Starting LSP Server...")
        self.lsp_client.start()
        
        try:
            print("[Pipeline] Initializing LSP Handshake...")
            self.lsp_client.initialize()
            
            # Send didOpen for all files so LSP server indexes them
            print("[Pipeline] Sending didOpen to LSP Server for files...")
            for file in files:
                abs_file = os.path.abspath(file)
                with open(abs_file, "r", encoding="utf-8") as f:
                    content = f.read()
                self.lsp_client.did_open(abs_file, content)

            # Give the language server a small window to index
            time.sleep(1.0)

            print("[Pipeline] Resolving definitions with LSP...")
            resolved_count = 0
            for call in all_calls:
                file_path = call["file_path"]
                callee = call["callee_name"]
                line = call["line"]
                col = call["column"]

                print(f"  Resolving call to '{callee}' at {os.path.basename(file_path)}:L{line} C{col}")
                try:
                    result = self.lsp_client.definition(file_path, line, col)
                    definition = self._parse_definition_response(result)
                    
                    if definition:
                        target_uri, target_line, target_col = definition
                        short_uri = target_uri.split('/')[-1]
                        print(f"    -> Found definition: {short_uri} L{target_line} C{target_col}")
                        self.db.insert_call_edge(
                            source_file=call["file_uri"],
                            source_line=line,
                            source_col=col,
                            callee_name=callee,
                            target_file=target_uri,
                            target_line=target_line,
                            target_col=target_col
                        )
                        resolved_count += 1
                    else:
                        print("    -> Definition not found (returned empty)")
                        self.db.insert_call_edge(
                            source_file=call["file_uri"],
                            source_line=line,
                            source_col=col,
                            callee_name=callee,
                            target_file=None,
                            target_line=None,
                            target_col=None
                        )
                except Exception as e:
                    print(f"    -> Error calling LSP: {e}")
                    self.db.insert_call_edge(
                        source_file=call["file_uri"],
                        source_line=line,
                        source_col=col,
                        callee_name=callee,
                        target_file=None,
                        target_line=None,
                        target_col=None
                    )

            print(f"[Pipeline] Finished. Successfully resolved {resolved_count}/{len(all_calls)} calls.")

        finally:
            print("[Pipeline] Shutting down LSP Server...")
            self.lsp_client.shutdown()

    def _parse_definition_response(self, result) -> Optional[Tuple[str, int, int]]:
        """Parses definition results matching Location or LocationLink forms."""
        if not result:
            return None
        
        # If list, take first match
        if isinstance(result, list):
            if not result:
                return None
            item = result[0]
        else:
            item = result

        # Location: { uri: string, range: Range }
        if "uri" in item and "range" in item:
            uri = item["uri"]
            start = item["range"]["start"]
            return uri, start["line"], start["character"]

        # LocationLink: { targetUri: string, targetSelectionRange: Range }
        if "targetUri" in item:
            uri = item["targetUri"]
            range_obj = item.get("targetSelectionRange", item.get("targetRange"))
            if range_obj:
                start = range_obj["start"]
                return uri, start["line"], start["character"]

        return None
