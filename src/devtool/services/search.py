import fnmatch
from pathlib import Path
from typing import Iterator

from devtool.utils.file_utils import safe_walk

def search_files(folder_path: Path, pattern: str) -> Iterator[Path]:
    """
    Search for files matching a specific pattern within a directory.
    Uses a generator to yield results lazily.
    """
    if not folder_path.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {folder_path}")

    # Use our memory-safe utility!
    for file_path in safe_walk(folder_path):
        # We use fnmatch to support wildcard patterns.
        # We compare lowercase versions so the search is case-insensitive.
        if fnmatch.fnmatch(file_path.name.lower(), pattern.lower()):
            yield file_path