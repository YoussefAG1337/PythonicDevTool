import logging
from rich.logging import RichHandler

def setup_logger(verbose: bool = False) -> None:
    """
    Configure the global logger.
    If verbose is True, set the level to DEBUG. Otherwise, INFO.
    """
    # Define our log format (Rich handles the timestamps and colors automatically!)
    log_format = "%(message)s"
    
    # Decide how noisy the app should be
    log_level = logging.DEBUG if verbose else logging.INFO

    logging.basicConfig(
        level=log_level,
        format=log_format,
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)]
    )