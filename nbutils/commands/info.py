"""
Info command - Show statistics and imports about a notebook
"""
from pathlib import Path
import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from nbutils.core.notebook import Notebook
from nbutils.core.cleaner import NotebookCleaner

console = Console()

@click.command()
@click.argument('notebook', type=click.Path(exists=True))
@click.option('--code-metrics', is_flag=True, help='Show code metrics')
@click.option('--imports', is_flag=True, help='Show imports')
def info(notebook, code_metrics, imports):
    """Show statistics and imports about a notebook"""
    try:
        nb_path = Path(notebook)
        nb = Notebook(nb_path)
        stats = nb.get_stats()
        console.print(f"\n[bold blue]Loading:[/bold blue] {nb_path.name}")
        table = Table(title=f"Statistics for {nb_path.name}", show_header=True, header_style="bold magenta")
        table.add_column("Metric", style="cyan", no_wrap=True)
        table.add_column("Value", style="green", justify="right")
        table.add_row("Total Cells", str(stats['total_cells']))
        table.add_row("Code Cells", str(stats['code_cells']))
        table.add_row("Markdown Cells", str(stats['markdown_cells']))
        table.add_row("Raw Cells", str(stats['raw_cells']))
        table.add_row("File Size", f"{stats['file_size']:,} bytes")
        console.print("\n")
        console.print(table)
        imports = nb.get_imports()
        console.print(f"\n[bold magenta]Imports:[/bold magenta]")
        if imports:
            for import_ in imports:
                console.print(f"- [green]{import_}[/green]")
        if code_metrics:
            code_metrics = nb.get_code_metrics()
            console.print(f"\n[bold magenta]Code Metrics:[/bold magenta]")
            table = Table(title=f"Code Metrics for {nb_path.name}", show_header=True, header_style="bold magenta")
            table.add_column("Metric", style="cyan", no_wrap=True)
            table.add_column("Value", style="green", justify="right")
            table.add_row("Total Lines", str(code_metrics['total_lines']))
            table.add_row("Code Cells", str(code_metrics['code_cells']))
    except Exception as e:
        console.print(f"\n[bold red]Error:[/bold red] {str(e)}")
        raise click.Abort()