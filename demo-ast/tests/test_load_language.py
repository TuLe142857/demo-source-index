from collections.abc import Sequence

from tree_sitter import Language
from demo_ast.parser import LanguageConfig, LanguageRegistry, UnsupportedLanguage


def test_load_language_by_factory_method(language_configs: Sequence[LanguageConfig]):
    for config in language_configs:
        lang = config.language_factory()
        assert isinstance(lang, Language)

def test_load_language_from_registry(language_configs: Sequence[LanguageConfig]):
    registry = LanguageRegistry(language_configs)
    for config in language_configs:
        lang = registry.get_language(config.name)
        assert isinstance(lang, Language)