"""
nbutils - A comprehensive, modern CLI toolkit that solves all major Jupyter notebook pain points in one unified interface.
Main CLI entry point
"""
import click
from rich.console import Console

console = Console()


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """nbutils"""
    pass


# Import commands
from nbutils.commands.clean import clean
from nbutils.commands.info import info
from nbutils.commands.export import export
from nbutils.commands.lint import lint

cli.add_command(clean)
cli.add_command(info)
cli.add_command(export)
cli.add_command(lint)


if __name__ == "__main__":
    cli()