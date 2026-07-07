from .language_registry import LanguageRegistry
from tree_sitter import Parser


class ParserFactory:
    def __init__(self, language_registry: LanguageRegistry):
        self._registry = language_registry

    def get_parser(self, language_name: str) -> Parser:
        language = self._registry.get_language(language_name)
        return Parser(language)

    def get_parser_for_file(self, filename: str) -> Parser:
        language = self._registry.get_language_for_file(filename)
        return Parser(language)
