import typer
from pathlib import Path
from rich.console import Console

from devtool.services.backup import create_backup

console = Console()

def backup_command(
    folder_path: Path = typer.Argument(
        ..., 
        help="Directory to backup", 
        exists=True, 
        file_okay=False, 
        resolve_path=True
    ),
    dest_path: Path = typer.Option(
        Path.home() / "devtool_backups", # Defaults to a folder in the user's home directory
        "--dest", 
        "-d", 
        help="Destination directory for the backup", 
        resolve_path=True
    ),
) -> None:
    """Create a timestamped zip backup of a directory."""
    try:
        # A Context Manager that renders an animated spinner!
        with console.status(f"[cyan]Compressing {folder_path.name}...[/cyan]", spinner="dots"):
            archive_path = create_backup(folder_path, dest_path)
            
        console.print(f"[bold green]✓ Backup created successfully![/bold green]")
        console.print(f"Saved to: [magenta]{archive_path}[/magenta]")
            
    except Exception as e:
        console.print(f"[bold red]Error creating backup:[/bold red] {e}")
        raise typer.Exit(code=1)