from collections.abc import Sequence

import pytest

from demo_ast.core import LanguageConfig, LanguageRegistry, ParserFactory
from demo_ast.languages import get_language_configs


@pytest.fixture(scope="session")
def language_configs() -> Sequence[LanguageConfig]:
    return get_language_configs()


@pytest.fixture(scope="session")
def language_registry(language_configs: Sequence[LanguageConfig]) -> LanguageRegistry:
    return LanguageRegistry(language_configs)


@pytest.fixture(scope="session")
def parser_factory(language_registry: LanguageRegistry) -> ParserFactory:
    return ParserFactory(language_registry)
