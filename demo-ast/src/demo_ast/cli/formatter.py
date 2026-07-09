from typing import Any, Protocol, TypeVar

T = TypeVar("T")


class Formatter[T](Protocol):
    def format(self, data: T) -> str:
        pass


class TreeFormatter(Formatter[dict]):
    SPACE = "   "
    VERTICAL = "│  "
    BRANCH = "├──"
    LAST_BRANCH = "└──"

    def _convert(self, data: Any) -> list[tuple[str, Any]]:
        if isinstance(data, dict):
            return list(data.items())
        elif isinstance(data, list) or isinstance(data, tuple):
            res = []
            for item in data:
                if isinstance(item, dict):
                    if len(item) == 0:
                        pass
                    elif len(item) == 1:
                        k, v = list(item.items())[0]
                        res.append((k, v))
                    else:
                        res.append(("", item))
                elif isinstance(item, list):
                    res.append(("", item))
                else:
                    res.append((str(item), None))
            return res
        else:
            return [
                (str(data), None),
            ]

    def _build_tree(self, lines: list[str], data, indent: str = ""):
        nodes = self._convert(data)
        for idx, (node_name, children) in enumerate(nodes):
            is_last_node = idx == len(nodes) - 1
            branch = self.LAST_BRANCH if is_last_node else self.BRANCH
            lines.append(f"{indent}{branch}{node_name}")

            if children is not None:
                children_indent = (
                    f"{indent}{self.SPACE if is_last_node else self.VERTICAL}"
                )
                self._build_tree(lines, children, children_indent)

    def format(self, data: Any) -> str:
        lines = []
        self._build_tree(lines, data)
        return "\n".join(lines)


if __name__ == "__main__":
    data = [
        {
            "function": {
                "name": "sum",
                "parameters": [
                    {
                        "positional_param": {
                            "type": "int",
                            "name": "a",
                        },
                    },
                    {
                        "positional_param": {
                            "type": "int",
                            "name": "a",
                        },
                    },
                    {
                        "keyword_param": {
                            "type": "int",
                            "name": "a",
                        },
                    },
                ],
            },
        },
        {
            "class": {
                "name": "Point",
                "attributes": [
                    {
                        "attribute": {
                            "type": "float",
                            "name": "x",
                        }
                    },
                    {"attribute": {"type": "float", "name": "y", "meta": None}},
                ],
            }
        },
        {"constant": {"type": "Point", "name": "p1"}},
        {"constant": {"type": "Point", "name": "p2"}},
        None,
    ]

    print(TreeFormatter().format(data))
