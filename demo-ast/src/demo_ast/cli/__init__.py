import typer
from .inspect_language import app as inspect_command
from .parse_code import app as parse_command

cli = typer.Typer()

cli.add_typer(inspect_command)
cli.add_typer(parse_command)


def run():
    cli()


if __name__ == "__main__":
    run()
