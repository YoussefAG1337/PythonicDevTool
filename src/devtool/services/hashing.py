import hashlib
from pathlib import Path


def calculate_file_hash(file_path: Path, algorithm: str = "sha256") -> str:
    """
    Calculate the hash of a file efficiently by reading it in chunks.

    Args:
        file_path: The path to the file to hash.
        algorithm: The hashing algorithm to use (e.g., 'sha256', 'md5').

    Returns:
        The hexadecimal hash string.

    Raises:
        ValueError: If the specified algorithm is not available.
        FileNotFoundError: If the file does not exist.
    """
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")

    # Check if the algorithm exists in hashlib
    if algorithm.lower() not in hashlib.algorithms_available:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    # Dynamically initialize the correct hash object (e.g., hashlib.sha256())
    hash_obj = hashlib.new(algorithm.lower())

    # 64KB chunks - a good balance between memory usage and IO speed
    chunk_size = 65536

    # Open in binary reading mode ("rb")
    with file_path.open("rb") as f:
        # A highly Pythonic way to read files in chunks until empty (b"")
        for chunk in iter(lambda: f.read(chunk_size), b""):
            hash_obj.update(chunk)

    return hash_obj.hexdigest()
