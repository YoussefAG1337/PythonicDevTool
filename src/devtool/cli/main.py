from devtool.commands.hash import hash_command
import logging
from devtool.commands.organize import organize_command
from devtool.utils.logger import setup_logger
from devtool.config.settings import load_config
from devtool.commands.stats import stats_command
from devtool.commands.search import search_command
from devtool.commands.backup import backup_command
from devtool.commands.clean import clean_command
import typer

# Initialize the main Typer application
app = typer.Typer(
    name="devtool",
    help="Dev Toolbox CLI - A professional utility belt for developers.",
    add_completion=False,
)

@app.callback()
def main_callback(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose debug logging.")
) -> None:
    """Dev Toolbox CLI - A professional utility belt for developers."""
    setup_logger(verbose)
    # Let's log a debug message to prove it works!
    config = load_config()
    logging.debug(f"Current theme is: {config.theme}")
    

app.command(name="hash")(hash_command)
app.command(name="stats")(stats_command)
app.command(name="search")(search_command)
app.command(name="organize")(organize_command)
app.command(name="backup")(backup_command)
app.command(name="clean")(clean_command)


def main() -> None:
    """Entry point for the CLI."""
    app()

if __name__ == "__main__":
    main()