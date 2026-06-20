from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from devtool.services.statistics import get_folder_stats

console = Console()


def stats_command(
    folder_path: Path = typer.Argument(
        ".",  # Default to the current directory if the user doesn't provide one
        help="Path to the directory to analyze",
        exists=True,
        file_okay=False,  # We only want folders!
        resolve_path=True,
    ),
) -> None:
    """Display statistics about files in a directory."""
    try:
        # 1. Get the raw data from our service layer
        stats = get_folder_stats(folder_path)

        # 2. Create a Rich Table
        table = Table(title=f"File Statistics for [cyan]{folder_path.name}[/cyan]")

        # Define our columns
        table.add_column("Extension", style="magenta")
        table.add_column("File Count", justify="right", style="green")

        # Sort extensions by count (highest first)
        sorted_extensions = sorted(
            stats.extension_counts.items(), key=lambda item: item[1], reverse=True
        )

        # Populate the table rows
        for ext, count in sorted_extensions:
            table.add_row(ext, str(count))

        # 3. Print the summary and the table
        size_mb = stats.total_size_bytes / (1024 * 1024)

        console.print(f"\n[bold]Total Files:[/bold] {stats.total_files}")
        console.print(f"[bold]Total Size:[/bold] {size_mb:.2f} MB\n")
        console.print(table)

    except NotADirectoryError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(code=1)
