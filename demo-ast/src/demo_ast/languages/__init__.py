from functools import lru_cache
from typing import Sequence

from demo_ast.core import LanguageConfig, LanguageRegistry

from . import c as C
from . import cpp as CPP
from . import go as GO
from . import java as JAVA
from . import javascript as JAVASCRIPT
from . import python as PYTHON
from . import rust as RUST
from . import typescript as TYPESCRIPT


@lru_cache
def get_language_configs() -> Sequence[LanguageConfig]:
    return (
        PYTHON.get_config(),
        JAVA.get_config(),
    )


@lru_cache
def get_language_registry() -> LanguageRegistry:
    return LanguageRegistry(get_language_configs())


__all__ = [
    "get_language_configs",
    "get_language_registry",
    "C",
    "CPP",
    "GO",
    "JAVA",
    "JAVASCRIPT",
    "PYTHON",
    "RUST",
    "TYPESCRIPT",
]
