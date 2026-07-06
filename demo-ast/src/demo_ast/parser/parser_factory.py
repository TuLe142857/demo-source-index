from .language_registry import LanguageRegistry
from tree_sitter import Parser


class ParserFactory:
    def __init__(self, language_registry: LanguageRegistry):
        self._registry = language_registry

    def get_parser_for_file(self, file_name: str) -> Parser:
        pass
