from demo_ast.parser import (
    UnsupportedLanguage,
    LanguageConfig,
    LanguageRegistry,
    ParserFactory,
)

from demo_ast.default_config import get_language_configs

language_configs = get_language_configs()
language_registry = LanguageRegistry(language_configs)
parser_factory = ParserFactory(language_registry)
