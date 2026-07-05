from collections.abc import Sequence

from tree_sitter import Language
import importlib
from functools import lru_cache

from demo_ast.parser import LanguageConfig


def get_language_from_module(
    module_name: str, method_name: str = "language"
) -> Language:
    """
    Args:
        module_name: name of module that provide language.
        method_name: callable attribute of module that provide language.
    Returns: Language
    """
    module = importlib.import_module(module_name)

    if not hasattr(module, method_name):
        raise RuntimeError(f"Module `{module_name}` has no attribute `{method_name}`")

    lang_create_func = getattr(module, method_name)
    if not callable(lang_create_func):
        raise RuntimeError(
            f"Attribute `{method_name}` in module `{module_name}` is not callable"
        )

    lang_object = lang_create_func()
    return Language(lang_object)


@lru_cache
def get_language_configs() -> Sequence[LanguageConfig]:
    """
    Returns: list of language configs
    """
    return (
        LanguageConfig(
            name="c",
            language_factory=lambda: get_language_from_module("tree_sitter_c"),
            extensions=[".c", ".h"],
        ),
        LanguageConfig(
            name="cpp",
            language_factory=lambda: get_language_from_module("tree_sitter_cpp"),
            extensions=[".cpp", ".hpp", ".cc", ".cxx", ".hh", ".hxx"],
        ),
        LanguageConfig(
            name="css",
            language_factory=lambda: get_language_from_module("tree_sitter_css"),
            extensions=[".css"],
        ),
        LanguageConfig(
            name="go",
            language_factory=lambda: get_language_from_module("tree_sitter_go"),
            extensions=[".go"],
        ),
        LanguageConfig(
            name="html",
            language_factory=lambda: get_language_from_module("tree_sitter_html"),
            extensions=[".html", ".htm"],
        ),
        LanguageConfig(
            name="java",
            language_factory=lambda: get_language_from_module("tree_sitter_java"),
            extensions=[".java"],
        ),
        LanguageConfig(
            name="javascript",
            language_factory=lambda: get_language_from_module("tree_sitter_javascript"),
            extensions=[".js", ".jsx", ".mjs", ".cjs"],
        ),
        LanguageConfig(
            name="json",
            language_factory=lambda: get_language_from_module("tree_sitter_json"),
            extensions=[".json"],
        ),
        LanguageConfig(
            name="python",
            language_factory=lambda: get_language_from_module("tree_sitter_python"),
            extensions=[".py", ".pyw"],
        ),
        LanguageConfig(
            name="rust",
            language_factory=lambda: get_language_from_module("tree_sitter_rust"),
            extensions=[".rs"],
        ),
        LanguageConfig(
            name="toml",
            language_factory=lambda: get_language_from_module("tree_sitter_toml"),
            extensions=[".toml"],
        ),
        LanguageConfig(
            name="yaml",
            language_factory=lambda: get_language_from_module("tree_sitter_yaml"),
            extensions=[".yaml", ".yml"],
        ),
    )
