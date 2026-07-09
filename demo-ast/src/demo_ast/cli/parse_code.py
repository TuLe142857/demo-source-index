from pathlib import Path
from typing import Annotated

import typer
from tree_sitter import Node

from demo_ast.core import ParserFactory, UASTNode
from demo_ast.languages import get_language_registry

app = typer.Typer()

language_registry = get_language_registry()
parser_factory = ParserFactory(language_registry)


# ├──
# └──
def inspect_cst(
    node: Node,
    level: int = 0,
    symbol: str = "├─",
    indent: str = "  ",
):
    print(f"{indent * level}{symbol}[{node.type}]")
    for idx, child in enumerate(node.children):
        if idx != (node.child_count - 1):
            inspect_cst(child, level + 1)
        else:
            inspect_cst(child, level + 1, symbol="└─")


def inspect_uast(node: UASTNode, level: int = 0):
    print(f"{'   ' * level}├──{node.kind}")
    print(f"{'   ' * level}|  {node.metadata}")
    for child in node.children:
        inspect_uast(child, level + 1)


@app.command(name="parse", help="Parse the code")
def parse(
    path: Annotated[str, typer.Argument(help="Path file code")],
):
    path = Path(path)
    if (not path.exists()) or (not path.is_file()):
        raise RuntimeError(f"Path {path} is not a file")

    # language = language_registry.get_language_for_file(path.name)
    # language_name = language.name
    # query_str = language_registry.language_configs[language_name].query_str
    # parser = parser_factory.get_parser(language_name)
