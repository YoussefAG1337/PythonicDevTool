import json
import logging
from dataclasses import asdict, dataclass
from pathlib import Path

# This resolves to C:\Users\YourName\.devtool_config.json on Windows, or ~/.devtool_config.json on Mac/Linux
CONFIG_FILE = Path.home() / ".devtool_config.json"


@dataclass
class Config:
    """Holds all configurable settings for the application."""

    default_hash_algorithm: str = "sha256"
    theme: str = "dark"
    # We will add more settings here as we build new features!


def load_config() -> Config:
    """Load configuration from disk, or return defaults if it doesn't exist."""
    if not CONFIG_FILE.exists():
        logging.debug("No config file found. Using defaults.")
        return Config()

    try:
        with CONFIG_FILE.open("r") as f:
            data = json.load(f)
        logging.debug(f"Loaded config from {CONFIG_FILE}")
        return Config(**data)
    except Exception as e:
        logging.error(f"Failed to load config: {e}. Using defaults.")
        return Config()


def save_config(config: Config) -> None:
    """Save the current configuration to disk."""
    with CONFIG_FILE.open("w") as f:
        json.dump(asdict(config), f, indent=4)
    logging.debug(f"Saved config to {CONFIG_FILE}")
