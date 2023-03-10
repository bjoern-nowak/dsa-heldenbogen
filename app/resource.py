from importlib.resources import as_file
from importlib.resources import files
from pathlib import Path
from typing import List


def list_files(filename: str) -> List[str]:
    return [f.name for f in files('resources').joinpath(filename).iterdir()]


def list_dirs(filename: str) -> List[str]:
    return [d.name for d in files('resources').joinpath(filename).iterdir() if d.is_dir()]


def get_path(filename: str) -> Path:
    with as_file(files('resources').joinpath(filename)) as filepath:
        return filepath


def get_abs_path(filename: str) -> str:
    with as_file(files('resources').joinpath(filename)) as filepath:
        return filepath.as_posix()
