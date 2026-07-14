import subprocess
import threading
import json
import queue
import os
from typing import Dict, Any, Optional

class LSPClient:
    """
    A lightweight LSP (Language Server Protocol) client that manages
    a server process via stdin/stdout and handles JSON-RPC requests/notifications.
    """
    def __init__(self, server_cmd: list[str], root_dir: str):
        self.server_cmd = server_cmd
        self.root_dir = root_dir
        self.process: Optional[subprocess.Popen] = None
        self.read_thread: Optional[threading.Thread] = None
        self.pending_requests: Dict[int, queue.Queue] = {}
        self.request_id = 0
        self.lock = threading.Lock()
        self.running = False

    def start(self):
        """Starts the language server process and response reading loop."""
        self.process = subprocess.Popen(
            self.server_cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            bufsize=0
        )
        self.running = True
        self.read_thread = threading.Thread(target=self._read_loop, daemon=True)
        self.read_thread.start()

    def _read_loop(self):
        """Background thread loop to continuously read and dispatch messages from LSP stdout."""
        stdout = self.process.stdout
        while self.running:
            try:
                content_length = None
                # Read headers
                while True:
                    line = stdout.readline()
                    if not line:
                        return  # EOF reached
                    line_str = line.decode('utf-8').strip()
                    if not line_str:
                        break  # End of headers (blank line)
                    if line_str.lower().startswith('content-length:'):
                        content_length = int(line_str.split(':')[1].strip())
                
                if content_length is None:
                    continue

                # Read exact bytes of the JSON body
                body_bytes = stdout.read(content_length)
                if len(body_bytes) < content_length:
                    return  # Premature EOF

                body_str = body_bytes.decode('utf-8')
                message = json.loads(body_str)

                # Dispatch if it is a response
                if 'id' in message:
                    msg_id = message['id']
                    with self.lock:
                        q = self.pending_requests.get(msg_id)
                    if q is not None:
                        q.put(message)
            except Exception:
                break

    def send_notification(self, method: str, params: Any):
        """Sends an LSP notification (no response expected)."""
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params
        }
        self._write_message(payload)

    def send_request(self, method: str, params: Any, timeout: float = 10.0) -> Any:
        """Sends an LSP request and blocks until the response is received or times out."""
        with self.lock:
            self.request_id += 1
            msg_id = self.request_id
            q = queue.Queue(maxsize=1)
            self.pending_requests[msg_id] = q

        payload = {
            "jsonrpc": "2.0",
            "id": msg_id,
            "method": method,
            "params": params
        }
        
        self._write_message(payload)
        
        try:
            response = q.get(timeout=timeout)
            with self.lock:
                self.pending_requests.pop(msg_id, None)
            if 'error' in response:
                raise RuntimeError(f"LSP Error: {response['error']}")
            return response.get('result')
        except queue.Empty:
            with self.lock:
                self.pending_requests.pop(msg_id, None)
            raise TimeoutError(f"Request {method} (id={msg_id}) timed out after {timeout}s")

    def _write_message(self, payload: Any):
        """Serializes and writes a JSON payload to the LSP server's stdin."""
        body = json.dumps(payload).encode('utf-8')
        header = f"Content-Length: {len(body)}\r\n\r\n".encode('utf-8')
        try:
            self.process.stdin.write(header + body)
            self.process.stdin.flush()
        except Exception as e:
            raise RuntimeError(f"Failed to write to LSP server: {e}")

    def initialize(self) -> Any:
        """Performs the standard LSP initialize/initialized handshake."""
        root_uri = f"file:///{os.path.abspath(self.root_dir).replace(os.sep, '/')}"
        params = {
            "processId": os.getpid(),
            "rootPath": os.path.abspath(self.root_dir),
            "rootUri": root_uri,
            "capabilities": {
                "textDocument": {
                    "definition": {
                        "dynamicRegistration": True,
                        "linkSupport": True
                    }
                }
            }
        }
        result = self.send_request("initialize", params)
        self.send_notification("initialized", {})
        return result

    def did_open(self, file_path: str, content: str):
        """Notifies LSP that a file was opened with the given content."""
        file_uri = f"file:///{os.path.abspath(file_path).replace(os.sep, '/')}"
        params = {
            "textDocument": {
                "uri": file_uri,
                "languageId": "python",
                "version": 1,
                "text": content
            }
        }
        self.send_notification("textDocument/didOpen", params)

    def definition(self, file_path: str, line: int, character: int) -> Any:
        """Queries the LSP server for the definition of the symbol at the given coordinate."""
        file_uri = f"file:///{os.path.abspath(file_path).replace(os.sep, '/')}"
        params = {
            "textDocument": {
                "uri": file_uri
            },
            "position": {
                "line": line,
                "character": character
            }
        }
        return self.send_request("textDocument/definition", params)

    def shutdown(self):
        """Gracefully shuts down the LSP server."""
        if self.process:
            try:
                self.send_request("shutdown", {}, timeout=2.0)
            except Exception:
                pass
            self.send_notification("exit", {})
            self.running = False
            self.process.terminate()
            try:
                self.process.wait(timeout=2.0)
            except Exception:
                self.process.kill()
