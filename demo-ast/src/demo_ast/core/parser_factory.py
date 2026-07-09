from tree_sitter import Parser

from demo_ast.core.language_registry import LanguageRegistry


class ParserFactory:
    def __init__(self, language_registry: LanguageRegistry):
        self._registry = language_registry

    def get_parser(self, language_name: str) -> Parser:
        language = self._registry.get_language(language_name)
        return Parser(language)

    def get_parser_for_file(self, filename: str) -> Parser:
        language = self._registry.get_language_for_file(filename)
        return Parser(language)
