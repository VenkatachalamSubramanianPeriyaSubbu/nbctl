"""
Merge command - Intelligent 3-way merge for notebook conflicts
"""
from pathlib import Path
import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from nbutils.core.merger import NotebookMerger

console = Console()


@click.command()
@click.argument('notebook1', type=click.Path(exists=True))
@click.argument('notebook2', type=click.Path(exists=True))
@click.option('-o', '--output', type=click.Path(), required=True,
              help='Output file for merged notebook')
@click.option('--strategy', type=click.Choice(['auto', 'ours', 'theirs', 'cell-append']),
              default='auto', help='Merge strategy')
@click.option('--backup/--no-backup', default=True,
              help='Create backup of output file if it exists')
@click.option('--report', is_flag=True, help='Show detailed merge report')
def merge(notebook1, notebook2, output, strategy, backup, report):
    """Combine two notebooks into one
    
    Simple 2-way merge that combines two notebooks.
    
    \b
    Strategies:
      auto        - Intelligently merge unique cells from both (default)
      ours        - Keep only the first notebook
      theirs      - Keep only the second notebook
      cell-append - Append all cells from both notebooks
    
    \b
    Examples:
      nbutils merge nb1.ipynb nb2.ipynb -o combined.ipynb
      nbutils merge nb1.ipynb nb2.ipynb -o combined.ipynb --strategy cell-append
    
    \b
    For 3-way merge with conflict detection, use 'nbutils resolve' instead.
    """
    try:
        console.print("[dim]Performing 2-way merge...[/dim]")
        nb1_path = Path(notebook1)
        nb2_path = Path(notebook2)
        output_path = Path(output)
        
        # For 2-way merge, use first notebook as both base and ours
        base_path = nb1_path
        ours_path = nb1_path
        theirs_path = nb2_path
        
        # Create backup if output exists
        if backup and output_path and output_path.exists():
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            backup_path = output_path.with_suffix(f".backup.{timestamp}.ipynb")
            import shutil
            shutil.copy2(output_path, backup_path)
            console.print(f"[dim]Created backup: {backup_path}[/dim]")
        
        # Create merger
        merger = NotebookMerger(base_path, ours_path, theirs_path)
        
        # Perform merge
        with console.status(f"[bold green]Merging notebooks using '{strategy}' strategy...[/bold green]"):
            merged = merger.merge(strategy=strategy)
        
        # Save merged notebook
        merger.save(output_path)
        
        # Display results
        if report:
            _display_merge_report(merger, output_path)
        else:
            console.print(f"\n[bold green]✓ Merge successful![/bold green]")
            console.print(f"Output: {output_path}")
            
            # Show brief stats
            stats = merger.get_statistics()
            console.print(f"\n[dim]Merged {stats['cells_merged']} cells, "
                         f"{stats['cells_from_ours']} from ours, "
                         f"{stats['cells_from_theirs']} from theirs[/dim]")
    
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        raise click.Abort()


def _display_merge_report(merger: NotebookMerger, output_path: Path):
    """Display detailed merge report"""
    stats = merger.get_statistics()
    
    console.print("\n[bold cyan]📊 Merge Report:[/bold cyan]\n")
    
    # Statistics table
    table = Table(show_header=False)
    table.add_column("Metric", style="cyan")
    table.add_column("Count", style="bold")
    
    table.add_row("Auto-merged cells", str(stats['cells_merged']))
    table.add_row("From first notebook", f"[blue]{stats['cells_from_ours']}[/blue]")
    table.add_row("From second notebook", f"[magenta]{stats['cells_from_theirs']}[/magenta]")
    table.add_row("Unchanged", f"[dim]{stats['cells_unchanged']}[/dim]")
    
    console.print(table)
    console.print(f"\n[bold]Output saved to:[/bold] {output_path}")

