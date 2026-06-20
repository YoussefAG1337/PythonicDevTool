import shutil
from pathlib import Path

# Define the exact names of the things we want to kill
JUNK_DIRS = {"__pycache__", ".pytest_cache", ".ruff_cache", ".mypy_cache"}
JUNK_FILES = {".DS_Store", "Thumbs.db"}


def find_junk(folder_path: Path) -> list[Path]:
    """Finds junk folders and files recursively."""
    if not folder_path.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {folder_path}")

    junk_paths = []
    for item in folder_path.rglob("*"):
        if item.is_dir() and item.name in JUNK_DIRS:
            junk_paths.append(item)
        elif item.is_file() and item.name in JUNK_FILES:
            junk_paths.append(item)

    return junk_paths


def delete_junk(junk_paths: list[Path]) -> int:
    """Deletes the provided paths safely. Returns the number of items deleted."""
    deleted_count = 0
    for path in junk_paths:
        if not path.exists():
            continue
        try:
            if path.is_dir():
                shutil.rmtree(path)  # Deletes a whole folder and everything inside
            else:
                path.unlink()  # Deletes a single file
            deleted_count += 1
        except Exception:
            # Skip files we don't have permission to delete (e.g. currently open files)
            pass

    return deleted_count
