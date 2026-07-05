from collections.abc import Sequence

from .language_config import LanguageConfig
from tree_sitter import Language


class LanguageRegistry:
    def __init__(self, configs: Sequence[LanguageConfig] | list[LanguageConfig]):
        # check duplicate language name
        # check duplicate extension for language
        # check duplicate file name pattern
        pass

    def get_supported_languages(self) -> Sequence[str]:
        pass

    def get_supported_file_extensions(self) -> Sequence[str]:
        pass

    def get_supported_file_patterns(self) -> Sequence[str]:
        pass

    def get_language(self, name: str) -> Language:
        pass

    def get_configs(self, name: str) -> Sequence[LanguageConfig]:
        # raise exc
        pass

    def resolve_name_for_file(self, file_name: str) -> str:
        # raise exc
        pass
