from collections.abc import Callable
from dataclasses import dataclass, field


from tree_sitter import Language


@dataclass(frozen=True)
class LanguageConfig:
    """
    Language config for loading custom tree-sitter languages.
    """

    name: str
    """Language name"""

    language_factory: Callable[[], Language]
    """Factory method to create language"""

    extensions: list[str] = field(default_factory=list)
    """List of language's file extensions. Default is empty list. Example: [".c", ".h"]"""

    filename_patterns: list[str] = field(default_factory=list)
    """List of language's file patterns. Default is empty list. Example: ["Dockerfile"]"""

    def __post_init__(self):
        pass
