from pathlib import Path

from typer.testing import CliRunner

from devtool.cli.main import app
from devtool.services.hashing import calculate_file_hash

# The CliRunner lets us simulate terminal commands in our tests
runner = CliRunner()


def test_calculate_file_hash_service(tmp_path: Path) -> None:
    """Test the pure business logic (Service Layer)"""
    # 1. Arrange: Create a temporary file with known content
    test_file = tmp_path / "test.txt"
    test_file.write_text("hello world")

    # 2. Act: Hash it using our service
    result = calculate_file_hash(test_file, "sha256")

    # 3. Assert: Verify it matches the known SHA256 for "hello world"
    expected_hash = "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
    assert result == expected_hash


def test_hash_cli_command(tmp_path: Path) -> None:
    """Test the CLI layer integration"""
    test_file = tmp_path / "test.txt"
    test_file.write_text("hello world")

    # Simulate a user running `devtool hash <path>` in the terminal
    result = runner.invoke(app, ["hash", str(test_file)])

    # Verify the command succeeded (exit code 0 means success in Linux/Windows)
    assert result.exit_code == 0
    # Verify our Rich formatting is printing the right stuff
    assert "SHA256" in result.stdout
    assert (
        "b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9"
        in result.stdout
    )
