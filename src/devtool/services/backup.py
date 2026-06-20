import shutil
from datetime import datetime
from pathlib import Path

def create_backup(folder_path: Path, dest_path: Path) -> Path:
    """
    Creates a zip archive of the given folder.
    Returns the path to the created archive.
    """
    if not folder_path.is_dir():
        raise NotADirectoryError(f"Path is not a directory: {folder_path}")

    # Ensure our backup destination exists (e.g., creating ~/devtool_backups if it doesn't)
    dest_path.mkdir(parents=True, exist_ok=True)

    # Create a timestamp like "20260620_143000"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"{folder_path.name}_{timestamp}"
    
    # shutil.make_archive needs the base path without the .zip extension
    base_name = str(dest_path / archive_name)
    
    # Do the heavy lifting
    archive_path_str = shutil.make_archive(base_name, 'zip', str(folder_path))
    
    return Path(archive_path_str)