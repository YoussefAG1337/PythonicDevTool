# Dev Toolbox CLI 🛠️

A professional, blazing-fast command-line utility belt designed for developers, built with Python 3.12, Typer, and Rich.

## Features

* **`hash`**: Cryptographically hash files with memory-efficient chunking.
* **`stats`**: Get a beautiful statistical breakdown of any directory.
* **`search`**: Recursively search for files using lazy generators.
* **`organize`**: Instantly clean up messy folders by sorting files by extension.
* **`backup`**: Create timestamped, zipped backups with progress spinners.
* **`clean`**: Safely eradicate developer junk (`__pycache__`, `.DS_Store`) with interactive confirmation.

## Architecture

This project follows a strict **Clean Architecture** pattern to maximize testability and maintainability:

* **`cli/`**: The Typer entry points (Routing and UI).
* **`commands/`**: The specific Typer command definitions (Argument parsing and Rich formatting).
* **`services/`**: The pure Python business logic (No printing, no Typer logic).

## Installation

We recommend using `uv` for lightning-fast global installation. Once installed, you can use the `devtool` command from anywhere on your computer.

`uv tool install devtool`

## Developer Guide

To contribute to this project, you will need `uv` installed.

1. Clone the repository.
2. Run `uv sync` to install all dependencies.
3. Run `uv run pytest` to execute the test suite.
4. Run `uv run ruff check` and `uv run mypy src` for linting and type checking.