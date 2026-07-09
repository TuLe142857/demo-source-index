from typing import Protocol

from tree_sitter import Tree

from .uast_node import UASTNode


class UASTConverter(Protocol):
    def convert(self, tree: Tree) -> UASTNode:
        pass
