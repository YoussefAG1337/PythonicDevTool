import shutil
from pathlib import Path


def organize_folder(folder_path: Path) -> dict[str, int]:
    """
    Organizes files in the root of the given folder into subfolders based on their extensions.
    Returns a dictionary of {extension: count_of_moved_files}.
    """
    if not folder_path.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {folder_path}")

    moved_stats: dict[str, int] = {}

    for item in folder_path.iterdir():
        # Only organize loose files, leave existing folders alone
        if item.is_file():
            # Get extension without the dot (e.g., 'pdf'), or 'others' if no extension
            ext = item.suffix.lower().lstrip(".") if item.suffix else "others"

            # Create the destination directory path
            dest_dir = folder_path / ext

            # Ensure the directory exists (exist_ok=True means it won't crash if it's already there)
            dest_dir.mkdir(exist_ok=True)

            # Move the file safely
            shutil.move(str(item), str(dest_dir / item.name))

            # Track statistics so our CLI can report what happened
            moved_stats[ext] = moved_stats.get(ext, 0) + 1

    return moved_stats
