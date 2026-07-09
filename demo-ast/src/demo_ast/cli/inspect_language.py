import dataclasses
import json
from collections.abc import Sequence
from pathlib import Path
from typing import Annotated, Any, Literal

import typer
from tabulate import tabulate
from tree_sitter import Language

from demo_ast.core import LanguageConfig
from demo_ast.languages import get_language_registry

from .formatter import Formatter

app = typer.Typer(name="language", help="Inspect language config")
language_registry = get_language_registry()


@app.command(name="ls", help="List available languages")
def list_languages(verbose: Annotated[bool, typer.Option("--verbose", "-v")] = False):
    for lang_name, lang_config in language_registry.language_configs.items():
        print(lang_name)
        if verbose:
            print(
                f"  File patterns: {lang_config.filename_patterns}",
                f"  File extension: {lang_config.extensions}",
                sep="\n",
            )


@dataclasses.dataclass
class NodeKindInfo:
    id: int
    """Node kind ID. Range: [0, Language.node_kind_count] """

    name: str | None
    """Node kind's name. To be None if node kind is not named node """

    is_named: bool
    """ """

    is_visible: bool
    """ """

    is_supertype: bool
    """ """

    subtype_ids: Sequence[int] = dataclasses.field(default_factory=list)
    """ """

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "is_named": self.is_named,
            "is_supertype": self.is_supertype,
            "subtype_ids": self.subtype_ids,
            "is_visible": self.is_visible,
        }


@dataclasses.dataclass
class FieldInfo:
    id: int
    """ Field's ID. Range: [0, Language.field_count] """

    name: str | None
    """Field's name. In most case, field has ID 0 will have name is None"""

    def to_dict(self) -> dict[str, Any]:
        return {"id": self.id, "name": self.name}


@dataclasses.dataclass
class LanguageInspection:
    name: str
    abi_version: int
    file_extensions: Sequence[str]
    file_patterns: Sequence[str]

    node_kinds: Sequence[NodeKindInfo]
    fields: Sequence[FieldInfo]

    # derived value
    node_kind_count: int = dataclasses.field(init=False)
    named_node_count: int = dataclasses.field(init=False)
    anonymous_node_count: int = dataclasses.field(init=False)
    visible_node_count: int = dataclasses.field(init=False)
    supertype_node_count: int = dataclasses.field(init=False)
    field_count: int = dataclasses.field(init=False)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "abi_version": self.abi_version,
            "file_extensions": self.file_extensions,
            "file_patterns": self.file_patterns,
            "node_kinds": [_.to_dict() for _ in self.node_kinds],
            "node_kind_count": self.node_kind_count,
            "named_node_count": self.named_node_count,
            "anonymous_node_count": self.anonymous_node_count,
            "visible_node_count": self.visible_node_count,
            "supertype_node_count": self.supertype_node_count,
            "fields": [_.to_dict() for _ in self.fields],
            "field_count": self.field_count,
        }

    def __post_init__(self):
        self.node_kind_count = len(self.node_kinds)
        self.named_node_count = len([_ for _ in self.node_kinds if _.is_named])
        self.anonymous_node_count = self.node_kind_count - self.named_node_count
        self.visible_node_count = len([_ for _ in self.node_kinds if _.is_visible])
        self.supertype_node_count = len([_ for _ in self.node_kinds if _.is_supertype])
        self.field_count = len(self.fields)

    @classmethod
    def from_language(
        cls, lang: Language, lang_config: LanguageConfig
    ) -> "LanguageInspection":
        node_kinds = [
            NodeKindInfo(
                id=idx,
                name=lang.node_kind_for_id(idx),
                is_named=lang.node_kind_is_named(idx),
                is_visible=lang.node_kind_is_visible(idx),
                is_supertype=lang.node_kind_is_supertype(idx),
                subtype_ids=lang.subtypes(idx),
            )
            for idx in range(lang.node_kind_count)
        ]

        fields = [
            FieldInfo(id=idx, name=lang.field_name_for_id(idx))
            for idx in range(lang.field_count)
        ]
        return LanguageInspection(
            name=lang_config.name,
            abi_version=lang.abi_version,
            file_extensions=lang_config.extensions,
            file_patterns=lang_config.filename_patterns,
            node_kinds=node_kinds,
            fields=fields,
        )


class LanguageInspectionFormatter(Formatter[LanguageInspection]):
    def __init__(self, verbose: bool = False):
        self._verbose = verbose

    @property
    def verbose(self) -> bool:
        return self._verbose

    @verbose.setter
    def verbose(self, verbose: bool):
        self._verbose = verbose


class MarkdownFormatter(LanguageInspectionFormatter):
    def format(self, data: LanguageInspection) -> str:
        def process_dict(d: dict[str, Any]) -> dict[str, Any]:
            for k, v in d.items():
                if v is None:
                    d[k] = "`None`"
                elif isinstance(v, str):
                    d[k] = (
                        v.replace("&", "&amp;")
                        .replace("<", "&lt;")
                        .replace(">", "&gt;")
                        .replace("|", "&#124;")
                        .replace("_", r"\_")
                        .replace("*", r"\*")
                        .replace("`", r"\`")
                    )
            return d

        nodes_data = [process_dict(_.to_dict()) for _ in data.node_kinds]
        fields_data = [process_dict(_.to_dict()) for _ in data.fields]

        node_kinds_table = tabulate(nodes_data, headers="keys", tablefmt="github")
        fields_table = tabulate(fields_data, headers="keys", tablefmt="github")

        return f"""
# {data.name.upper()}\n
- Language: {data.name}
- ABI version: {data.abi_version}
- File name extensions: {list(data.file_extensions)}
- File name patterns: {list(data.file_patterns)}
- Node kinds count: {data.node_kind_count}
    - Anonymous node count: {data.anonymous_node_count}
    - Visible node count: {data.visible_node_count}
    - Supertype node count: {data.supertype_node_count}
- Field count: {data.field_count}

## Node kinds\n
{node_kinds_table}\n
## Fields\n
{fields_table}
"""


class JSONFormatter(LanguageInspectionFormatter):
    def format(self, data: LanguageInspection) -> str:
        dict_data = data.to_dict()
        return json.dumps(dict_data, indent=2)


class PlainFormatter(LanguageInspectionFormatter):
    def format(self, data: LanguageInspection) -> str:
        def process_dict(d: dict[str, Any]) -> dict[str, Any]:
            for k, v in d.items():
                if isinstance(v, str):
                    d[k] = (
                        v.replace("\n", "\\n").replace("\r", "\\r").replace("\t", "\\t")
                    )
            return d

        nodes_data = [process_dict(_.to_dict()) for _ in data.node_kinds]
        fields_data = [process_dict(_.to_dict()) for _ in data.fields]

        node_kinds_table = tabulate(
            nodes_data, headers="keys", tablefmt="rounded_grid", maxcolwidths=20
        )
        fields_table = tabulate(fields_data, headers="keys", tablefmt="rounded_grid")

        return f"""
# {data.name.upper()}\n
- Language: {data.name}
- ABI version: {data.abi_version}
- File name extensions: {list(data.file_extensions)}
- File name patterns: {list(data.file_patterns)}
- Node kinds count: {data.node_kind_count}
    - Anonymous node count: {data.anonymous_node_count}
    - Visible node count: {data.visible_node_count}
    - Supertype node count: {data.supertype_node_count}
- Field count: {data.field_count}

## Node kinds\n
{node_kinds_table}\n
## Fields\n
{fields_table}
        """


FORMATTERS: dict[str, LanguageInspectionFormatter] = {
    "markdown": MarkdownFormatter(),
    "json": JSONFormatter(),
    "plain": PlainFormatter(),
}


@app.command(name="inspect", help="Inspect language")
def inspect_language(
    name: Annotated[
        str, typer.Argument(help="Language name. Use 'all' to inspect all languages.")
    ],
    verbose: Annotated[bool, typer.Option("--verbose", "-v")] = False,
    file: Annotated[str | None, typer.Option("--file", "-f")] = None,
    fmt: Annotated[
        Literal["plain", "markdown", "json"], typer.Option("--format", "-fmt")
    ] = "plain",
):
    formatter = FORMATTERS[fmt]
    formatter.verbose = verbose

    result: str
    if name == "all":
        results = [
            formatter.format(
                LanguageInspection.from_language(
                    language_registry.get_language(lang_name), lang_config
                )
            )
            for lang_name, lang_config in language_registry.language_configs.items()
        ]
        result = (
            "\n".join(results)
            if fmt != "json"
            else json.dumps([json.loads(_) for _ in results], indent=2)
        )

    else:
        result = formatter.format(
            LanguageInspection.from_language(
                language_registry.get_language(name),
                language_registry.language_configs[name],
            )
        )

    if file is not None:
        path = Path(file)
        path.write_text(result)
    else:
        print(result)
