from collections.abc import Iterator
from pathlib import Path

# Folders we almost never want to scan
IGNORE_DIRS = {
    ".venv",
    "venv",
    "env",
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
}


def safe_walk(folder_path: Path) -> Iterator[Path]:
    """
    A generator that yields files in a directory, skipping ignored folders.
    This is much faster and safer than rglob("*").
    """
    if not folder_path.is_dir():
        return

    # iterdir() gets the direct children of the current folder
    for item in folder_path.iterdir():
        if item.is_dir():
            if item.name not in IGNORE_DIRS:
                # Recursively yield from subdirectories
                yield from safe_walk(item)
        elif item.is_file():
            yield item
