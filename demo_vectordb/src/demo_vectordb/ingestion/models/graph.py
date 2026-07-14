from dataclasses import dataclass, field
from typing import Any, Dict
from enum import Enum

@dataclass
class Node:
    project: str
    qualified_name: str
    label: str           
    name: str
    file_path: str = ""
    start_line: int = 0
    end_line: int = 0
    properties: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Edge:
    project: str
    source_qn: str
    target_qn: str
    type: str            
    properties: Dict[str, Any] = field(default_factory=dict)

class NodeType(str, Enum):
    """Định nghĩa các loại Node dựa trên cấu trúc thư mục, hệ thống file và Tree-Sitter AST."""
    PROJECT = "Project"
    PACKAGE = "Package"
    FOLDER = "Folder"
    FILE = "File"
    MODULE = "Module"
    FUNCTION = "Function"
    METHOD = "Method"
    CLASS = "Class"
    INTERFACE = "Interface"
    ENUM = "Enum"
    TYPE = "Type"
    ROUTE = "Route"

class EdgeType(str, Enum):
    """Định nghĩa các loại Edge thể hiện ngữ nghĩa giữa các Node."""
    # Invocation
    CALLS = "CALLS"
    HTTP_CALLS = "HTTP_CALLS"
    ASYNC_CALLS = "ASYNC_CALLS"
    
    # Module import
    IMPORTS = "IMPORTS"
    
    # Structural nesting
    CONTAINS = "CONTAINS" # Dùng làm prefix cho các loại CONTAINS_* động
    DEFINES = "DEFINES"
    DEFINES_METHOD = "DEFINES_METHOD"
    
    # Interface impl. & OOP hierarchy
    IMPLEMENTS = "IMPLEMENTS"
    INHERITS = "INHERITS"
    DECORATES = "DECORATES"
    
    # Route -> handler
    HANDLES = "HANDLES"
    
    # Symbol reference
    USES_TYPE = "USES_TYPE"
    USAGE = "USAGE"
    
    # Side effects
    THROWS = "THROWS"
    READS = "READS"
    WRITES = "WRITES"
    
    # Config linkage & Semantic links & Community membership
    CONFIGURES = "CONFIGURES"
    TESTS = "TESTS"
    FILE_CHANGES_WITH = "FILE_CHANGES_WITH"
    MEMBER_OF = "MEMBER_OF"