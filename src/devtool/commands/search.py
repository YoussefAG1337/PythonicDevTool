from pathlib import Path

import typer
from rich.console import Console

from devtool.services.search import search_files

console = Console()


def search_command(
    # The pattern is required!
    pattern: str = typer.Argument(..., help="Search pattern (e.g., '*.py', 'main*')"),
    # The directory is optional, defaulting to "."
    folder_path: Path = typer.Option(
        ".",
        "--dir",
        "-d",
        help="Directory to search in",
        exists=True,
        file_okay=False,
        resolve_path=True,
    ),
) -> None:
    """Search recursively for files matching a pattern."""
    try:
        console.print(
            f"Searching for [bold magenta]'{pattern}'[/bold magenta] in [cyan]{folder_path.name}[/cyan]..."
        )

        results_found = 0

        # Because search_files is a generator, we process and print matches the millisecond they are found!
        for matched_file in search_files(folder_path, pattern):
            results_found += 1
            # Print the path relative to the searched directory so it's easier to read
            rel_path = matched_file.relative_to(folder_path)
            console.print(f"[green]✓[/green] {rel_path}")

        if results_found == 0:
            console.print("[yellow]No files matched your search.[/yellow]")
        else:
            console.print(f"\n[bold]Total found:[/bold] {results_found}")

    except NotADirectoryError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(code=1)
