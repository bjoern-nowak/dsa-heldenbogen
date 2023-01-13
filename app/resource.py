from importlib.resources import as_file
from importlib.resources import files
from pathlib import Path


def get_path(filename: str) -> Path:
    with as_file(files('resources').joinpath(filename)) as filepath:
        return filepath


def get_abs_path(filename: str) -> str:
    with as_file(files('resources').joinpath(filename)) as filepath:
        return filepath.as_posix()
