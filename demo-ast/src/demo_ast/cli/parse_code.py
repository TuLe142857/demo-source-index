from typing import Annotated

import typer
from .config import parser_factory
from pathlib import Path
from tree_sitter import Node

app = typer.Typer()


def inspect_node(node: Node, depth: int = 0, named_only: bool = False, limit: int = -1):
    print(
        f"{'  ' * depth + '- '}Type: '{node.type}'({'NamedNode' if node.is_named else 'AnonymousNode'}; id={node.grammar_id}; name={node.grammar_name})",
        f"{'  ' * depth + '  '}Child count: {node.child_count}({node.named_child_count} named node, {node.child_count - node.named_child_count} anonymous nodes)",
        sep="\n",
    )
    if limit == depth:
        return
    for child in node.children:
        if named_only and (not child.is_named):
            continue
        inspect_node(child, depth + 1, named_only, limit)


@app.command(name="parse", help="Parse the code")
def parse(
    path: Annotated[str, typer.Argument(help="Path file code")],
    named_only: Annotated[
        bool, typer.Option("--named", help="display only named node")
    ] = False,
    limit: Annotated[int, typer.Option("-L", help="Limit depth")] = 0,
):
    path = Path(path)
    if (not path.exists()) or (not path.is_file()):
        raise RuntimeError(f"Path {path} is not a file")
    parser = parser_factory.get_parser_for_file(path.name)
    tree = parser.parse(path.read_bytes())
    inspect_node(tree.root_node, 0, named_only, limit=limit - 1)
