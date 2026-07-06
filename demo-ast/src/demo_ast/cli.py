from typing import Annotated
from .default_config import get_language_configs
from demo_ast.parser import LanguageRegistry, ParserFactory
import typer

cli = typer.Typer()
LANGUAGE_CONFIGS = get_language_configs()
registry = LanguageRegistry(LANGUAGE_CONFIGS)
factory = ParserFactory(registry)


@cli.command()
def run(path: Annotated[str, typer.Argument(help="file path")] = ".") -> None:
    pass
    # path = Path(path)
    # if not path.exists():
    #     print(f"File not found: '{path}'")
    #     return
    # if not path.is_file():
    #     print(f"Path is not a file: '{path}'")
    #     return
    #
    # print(
    #     f"File path(absolute): '{path.absolute()}'",
    #     f"File name: '{path.name}'",
    #     f"File extension: '{path.suffix}'",
    #     sep="\n"
    # )
    #
    # content = path.read_bytes()
    # parser = parser_provider.get_parser_for_file(path.name)
    # tree = parser.parse(content)
    # print(tree)
