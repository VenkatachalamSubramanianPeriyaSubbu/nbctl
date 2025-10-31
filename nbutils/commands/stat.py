"""
Stat command - Show statistics about a notebook
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
def stat(notebook):
    """Show statistics about a notebook"""
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
        
    except Exception as e:
        console.print(f"\n[bold red]Error:[/bold red] {str(e)}")
        raise click.Abort()