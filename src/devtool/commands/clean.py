from pathlib import Path

import typer
from rich.console import Console

from devtool.services.clean import delete_junk, find_junk

console = Console()


def clean_command(
    folder_path: Path = typer.Argument(
        ".", help="Directory to clean", exists=True, file_okay=False, resolve_path=True
    ),
    force: bool = typer.Option(
        False, "--force", "-f", help="Don't ask for confirmation"
    ),
) -> None:
    """Safely delete temporary developer files (e.g., __pycache__)."""
    try:
        console.print(f"Scanning [cyan]{folder_path.name}[/cyan] for developer junk...")
        junk_paths = find_junk(folder_path)

        if not junk_paths:
            console.print("[green]Your directory is already perfectly clean![/green]")
            return

        console.print(f"[yellow]Found {len(junk_paths)} junk files/folders.[/yellow]")

        # Interactive confirmation!
        if not force:
            confirm = typer.confirm("Are you sure you want to permanently delete them?")
            if not confirm:
                console.print("Clean aborted. Your files are safe.")
                raise typer.Abort()

        deleted = delete_junk(junk_paths)
        console.print(f"[bold green]Successfully deleted {deleted} items![/bold green]")

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(code=1)
