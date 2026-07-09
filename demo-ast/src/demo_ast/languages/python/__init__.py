from functools import lru_cache
from pathlib import Path

import tree_sitter_python
from tree_sitter import Language

from demo_ast.core import LanguageConfig


@lru_cache
def get_query_str() -> str:
    cwd = Path(__file__).resolve().parent
    query_path = cwd.joinpath("query.scm")
    return query_path.read_text(encoding="utf-8")


@lru_cache
def get_config() -> LanguageConfig:
    return LanguageConfig(
        name="python",
        language_factory=lambda: Language(tree_sitter_python.language()),
        extensions=[".py"],
        query_str=get_query_str(),
    )


__all__ = ["get_query_str", "get_config"]
