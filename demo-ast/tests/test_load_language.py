from tree_sitter import Language

from demo_ast.default_config import get_language_configs
import pytest
import importlib


@pytest.mark.parametrize(
    "module_name",
    [
        "tree_sitter_c",
        "tree_sitter_cpp",
        "tree_sitter_css",
        "tree_sitter_go",
        "tree_sitter_html",
        "tree_sitter_java",
        "tree_sitter_javascript",
        "tree_sitter_json",
        "tree_sitter_python",
        "tree_sitter_rust",
        "tree_sitter_toml",
        "tree_sitter_yaml",
    ],
)
def test_load_module(module_name: str):
    module = importlib.import_module(module_name)
    assert hasattr(module, "language")
    factory_func = getattr(module, "language")
    assert callable(factory_func)


def test_load_language():
    for config in get_language_configs():
        lang = config.language_factory()
        assert isinstance(lang, Language)
