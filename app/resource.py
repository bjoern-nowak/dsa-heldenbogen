from importlib.resources import as_file
from importlib.resources import files
from typing import List


def list_files(folder: str) -> List[str]:
    """
    List files under given folder
    :param folder: (relative to 'resources' folder) can be path-like, eg. "foo/bar"
    :return: all found files by name
    """
    return [f.name for f in files('resources').joinpath(folder).iterdir()]


def list_dirs(folder: str) -> List[str]:
    """
    List sub-folders under given folder
    :param folder: (relative to 'resources' folder) can be path-like, eg. "foo/bar"
    :return: all sub-folders by name
    """
    return [d.name for d in files('resources').joinpath(folder).iterdir() if d.is_dir()]

def get_path(filename: str) -> Path:
    with as_file(files('resources').joinpath(filename)) as filepath:
        return filepath

def get_abs_path(path: str) -> str:
    """
    :param path: (relative to 'resources' folder) can be a folder or file, path-like, eg. "foo/bar"
    :return: absolute path string
    """
    with as_file(files('resources').joinpath(path)) as filepath:
        return filepath.as_posix()
