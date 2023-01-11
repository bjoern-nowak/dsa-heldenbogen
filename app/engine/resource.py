from importlib.resources import as_file
from importlib.resources import files


def get_abs_path(filename: str) -> str:
    with as_file(files('resources').joinpath(filename)) as filepath:
        return filepath.as_posix()
