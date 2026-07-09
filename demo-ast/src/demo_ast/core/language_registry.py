import fnmatch
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Mapping, Sequence

from tree_sitter import Language

from .exception import UnsupportedLanguage


@dataclass(frozen=True)
class LanguageConfig:
    """
    Language config for loading custom tree-sitter languages.
    """

    name: str
    """Language name"""

    language_factory: Callable[[], Language]
    """Factory method to create language"""

    query_str: str = field(default="")
    """Language query string"""

    extensions: Sequence[str] = field(default_factory=list)
    """
    List of language's file extensions.
    Default is empty list. Example: [".c", ".h"]
    """

    filename_patterns: Sequence[str] = field(default_factory=list)
    """
    List of language's file patterns.
    Default is empty list. Example: ["Dockerfile"]
    """

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

        match_pattern = any(
            [fnmatch.fnmatch(path.name, pattern) for pattern in self.filename_patterns]
        )
        match_extension = path.suffix in self.extensions
        return match_pattern or match_extension


class LanguageRegistry:
    def __init__(self, configs: Sequence[LanguageConfig] | list[LanguageConfig]):
        # check duplicate: language name, ext, pattern
        language_names = [config.name for config in configs]
        language_patterns = [
            pattern for config in configs for pattern in config.filename_patterns
        ]
        language_extensions = [
            extension for config in configs for extension in config.extensions
        ]

        if len(language_names) != len(set(language_names)):
            duplicates = [
                name for name, count in Counter(language_names).items() if count > 1
            ]
            raise ValueError(f"Duplicate language names: {duplicates}")

        if len(language_patterns) != len(set(language_patterns)):
            duplicates = [
                name for name, count in Counter(language_patterns).items() if count > 1
            ]
            raise ValueError(f"Duplicate language patterns: {duplicates}")

        if len(language_extensions) != len(set(language_extensions)):
            duplicates = [
                name
                for name, count in Counter(language_extensions).items()
                if count > 1
            ]
            raise ValueError(f"Duplicate language extensions: {duplicates}")

        self._configs: dict[str, LanguageConfig] = {
            config.name: config for config in configs
        }
        self._supported_languages: Sequence[str] = tuple(language_names)
        self._supported_file_patterns: Sequence[str] = tuple(language_patterns)
        self._supported_file_extensions = tuple(language_patterns)
        self._languages_cache: dict[str, Language] = {}

    @property
    def supported_languages(self) -> Sequence[str]:
        return self._supported_languages

    @property
    def supported_file_patterns(self) -> Sequence[str]:
        return self._supported_file_patterns

    @property
    def supported_file_extensions(self) -> Sequence[str]:
        return self._supported_file_extensions

    @property
    def language_configs(self) -> Mapping[str, LanguageConfig]:
        """

        Returns: Mapping[language_name, LanguageConfig]

        """
        return self._configs

    def get_language(self, name: str) -> Language:
        if name not in self._configs:
            raise UnsupportedLanguage(name)
        lang = self._languages_cache.get(name)
        if lang is None:
            config = self._configs[name]
            lang = config.language_factory()
            self._languages_cache[name] = lang
        return lang

    def get_language_for_file(self, filename: str) -> Language:
        name = self.resolve_language_name_for_file(filename)
        return self.get_language(name)

    def resolve_language_name_for_file(self, filename: str) -> str:
        for name, config in self._configs.items():
            if config.match(filename):
                return name
        raise UnsupportedLanguage(f"No language supported for filename {filename}")
