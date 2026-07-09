from pathlib import Path
from typing import Annotated, Any

import typer
from tree_sitter import Node

from demo_ast.core import ParserFactory
from demo_ast.languages import get_language_registry

from .formatter import TreeFormatter

app = typer.Typer()

language_registry = get_language_registry()
parser_factory = ParserFactory(language_registry)


def cst_to_dict(
    node: Node,
    *,
    limit: int = -1,
    named_only: bool = False,
    excludes: list[str] | None = None,
) -> dict[str, Any] | None:

    if (named_only and not node.is_named) or (
        excludes is not None and node.type in excludes
    ):
        return None

    if (limit == 0) or (node.child_count == 0):
        return {f"{node.type}": None}

    tree = {f"{node.type}": []}
    for idx in range(node.child_count):
        children = node.child(idx)
        if children is None:
            continue
        subtree = cst_to_dict(
            children, limit=limit - 1, named_only=named_only, excludes=excludes
        )
        if subtree is not None:
            tree[f"{node.type}"].append(subtree)
    return tree


@app.command(name="parse", help="Parse the code")
def parse(
    path: Annotated[str, typer.Argument(help="Path to source code(file)")],
    limit: Annotated[int, typer.Option("--limit", help="Depth limit")] = -1,
    named_only: Annotated[
        bool, typer.Option("--named-only", help="Exclude anonymous node")
    ] = False,
    excludes: Annotated[
        list[str] | None, typer.Option("--exclude", help="Exclude node type")
    ] = None,
):
    path = Path(path)
    if (not path.exists()) or (not path.is_file()):
        raise RuntimeError(f"Path {path} is not a file")

    content = path.read_bytes()

    language_name = language_registry.resolve_language_name_for_file(path.name)
    parser = parser_factory.get_parser(language_name)

    cst_tree = parser.parse(content)
    cst_tree_str = cst_to_dict(
        cst_tree.root_node, limit=limit, named_only=named_only, excludes=excludes
    )

    formatter = TreeFormatter()
    print(formatter.format(cst_tree_str))
