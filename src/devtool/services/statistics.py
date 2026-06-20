from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class FolderStats:
    """A strongly-typed data container for our statistics."""

    total_files: int = 0
    total_size_bytes: int = 0
    # We use a default_factory for mutable types like dictionaries
    extension_counts: dict[str, int] = field(default_factory=dict)


def get_folder_stats(folder_path: Path) -> FolderStats:
    """
    Recursively calculate statistics for a given folder.

    Raises:
        NotADirectoryError: If the path does not point to a valid directory.
    """
    if not folder_path.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {folder_path}")

    stats = FolderStats()

    # .rglob("*") recursively finds ALL files and folders inside the path
    for item in folder_path.rglob("*"):
        if item.is_file():
            stats.total_files += 1
            stats.total_size_bytes += item.stat().st_size

            # Get the extension (e.g. '.py'), defaulting to 'No Extension'
            ext = item.suffix.lower() if item.suffix else "No Extension"

            # Increment the count for this extension
            stats.extension_counts[ext] = stats.extension_counts.get(ext, 0) + 1

    return stats
