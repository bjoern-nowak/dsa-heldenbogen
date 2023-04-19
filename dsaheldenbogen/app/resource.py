from importlib.resources import as_file
from importlib.resources import files
from typing import List


class Resource:
    RESOURCE_ROOT: str = 'resources'

    @classmethod
    def list_files(cls, folder: str) -> List[str]:
        """
        List files under given folder
        :param folder: (relative to 'resources' folder) can be path-like, eg. "foo/bar"
        :return: all found files by name
        """
        return [f.name for f in files(cls.RESOURCE_ROOT).joinpath(folder).iterdir()]

    @classmethod
    def list_dirs(cls, folder: str) -> List[str]:
        """
        List sub-folders under given folder
        :param folder: (relative to 'resources' folder) can be path-like, eg. "foo/bar"
        :return: all sub-folders by name
        """
        return [d.name for d in files(cls.RESOURCE_ROOT).joinpath(folder).iterdir() if d.is_dir()]

    @classmethod
    def get_abs_path(cls, path: str) -> str:
        """
        :param path: (relative to 'resources' folder) can be a folder or file, path-like, eg. "foo/bar"
        :return: absolute path string
        """
        with as_file(files(cls.RESOURCE_ROOT).joinpath(path)) as filepath:
            return filepath.as_posix()
