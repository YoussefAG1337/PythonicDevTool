from pathlib import Path

import typer
from rich.console import Console

from devtool.services.hashing import calculate_file_hash

# We use Rich's Console to print beautiful, colored output
console = Console()


def hash_command(
    # Typer magically turns these type hints into CLI arguments and validates them!
    file_path: Path = typer.Argument(
        ...,
        help="Path to the file to hash",
        exists=True,  # Typer will error immediately if file doesn't exist
        dir_okay=False,  # Typer will error if it's a directory
        resolve_path=True,  # Converts to an absolute path automatically
    ),
    algorithm: str = typer.Option(
        "sha256",
        "--algo",
        "-a",
        help="Hashing algorithm to use (e.g., md5, sha1, sha256)",
    ),
) -> None:
    """Calculate the cryptographic hash of a file."""
    try:
        # 1. Call the service layer
        result = calculate_file_hash(file_path, algorithm)

        # 2. Print pretty output
        console.print(
            f"[bold green]{algorithm.upper()}[/bold green] hash for [cyan]{file_path.name}[/cyan]:"
        )
        console.print(result)

    except ValueError as e:
        # Catch the ValueError we defined in our service and print it nicely
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(code=1)
