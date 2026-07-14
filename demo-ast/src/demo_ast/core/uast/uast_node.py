from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from typing import List, Optional, Any, Dict, Literal

@dataclass
class Position:
    row: int
    column: int

@dataclass(kw_only=True)
class UASTNode:
    """Base class for UAST (Unified Abstract Syntax Tree) nodes."""

    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    """Unique UUID"""

    node_type: str
    
    start_point: Position
    end_point: Position
    start_byte: int
    end_byte: int
    
    language: str | None = None

    name: str = ""
    """Name(identifier) of the node"""

    file_path: str | None = None
    """File path of the node"""
    
    source_code: str | None = None
    docstring: str | None = None
    
    parent_id: str | None = None
    children: List[UASTNode] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass(kw_only=True)
class FileNode(UASTNode):
    node_type: Literal["file"] = "file"
    imports: List[ImportNode] = field(default_factory=list)

@dataclass(kw_only=True)
class FunctionNode(UASTNode):
    node_type: Literal["function", "method"] = "function"
    parameters: List[str] = field(default_factory=list)
    return_type: Optional[str] = None
    is_async: bool = False
    modifiers: List[str] = field(default_factory=list)
    calls: List[str] = field(default_factory=list)

@dataclass(kw_only=True)
class ClassNode(UASTNode):
    node_type: Literal["class", "interface", "struct", "trait", "enum"] = "class"
    base_classes: List[str] = field(default_factory=list)
    modifiers: List[str] = field(default_factory=list)

@dataclass(kw_only=True)
class VariableNode(UASTNode):
    node_type: Literal["variable", "field", "constant"] = "variable"
    data_type: Optional[str] = None
    is_global: bool = False
    value: Optional[str] = None

@dataclass(kw_only=True)
class ImportNode(UASTNode):
    node_type: Literal["import"] = "import"
    module_source: str = ""
    imported_names: List[str] = field(default_factory=list)
    is_wildcard: bool = False
