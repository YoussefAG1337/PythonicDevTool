import typer
from pathlib import Path
from rich.console import Console

from devtool.services.organize import organize_folder

console = Console()

def organize_command(
    folder_path: Path = typer.Argument(
        ..., 
        help="Path to the directory to organize", 
        exists=True, 
        file_okay=False, 
        resolve_path=True
    ),
) -> None:
    """Organize loose files into folders by their extensions."""
    try:
        console.print(f"Organizing files in [cyan]{folder_path.name}[/cyan]...")
        
        stats = organize_folder(folder_path)
        
        if not stats:
            console.print("[yellow]No loose files found to organize.[/yellow]")
            return
            
        for ext, count in stats.items():
            console.print(f"[green]✓[/green] Moved {count} file(s) to [bold]{ext}/[/bold]")
            
        total_moved = sum(stats.values())
        console.print(f"\n[bold green]Successfully organized {total_moved} files![/bold green]")
            
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred:[/bold red] {e}")
        raise typer.Exit(code=1)