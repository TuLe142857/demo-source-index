from collections.abc import Callable, Sequence
from dataclasses import dataclass, field

import fnmatch
from pathlib import Path
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

    extensions: Sequence[str] = field(default_factory=list)
    """List of language's file extensions. Default is empty list. Example: [".c", ".h"]"""

    filename_patterns: Sequence[str] = field(default_factory=list)
    """List of language's file patterns. Default is empty list. Example: ["Dockerfile"]"""

    def __post_init__(self):
        if len(self.extensions) != len(set(self.extensions)):
            raise ValueError("Duplicate extensions")

        if len(self.filename_patterns) != len(set(self.filename_patterns)):
            raise ValueError("Duplicate filename patterns")

    def match(self, filename: str) -> bool:
        """
        Check if filename matches this language(match patterns or extensions).
        Args:
            filename: Filename can contain directory with separator.
        Returns: `true` if filename matches this language, `false` otherwise.
        """
        path = Path(filename)

        match_pattern = any([fnmatch.fnmatch(path.name, pattern) for pattern in self.filename_patterns])
        match_extension = path.suffix in self.extensions
        return match_pattern or match_extension