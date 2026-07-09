from dataclasses import dataclass, field
from typing import Any


@dataclass
class UASTNode:
    """
    Base class for UAST(Unified Abstract Syntax Tree) nodes.
    """

    id: int

    kind: str
    native_kind: str
    language: str | None

    point_range: tuple[tuple[int, int], tuple[int, int]]
    byte_range: tuple[int, int]

    doc: str | None = field(default=None)
    text: str | None = field(default=None)

    parent_id: int | None = field(default=None)
    parent: "UASTNode | None" = field(default=None)
    children: list["UASTNode"] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
