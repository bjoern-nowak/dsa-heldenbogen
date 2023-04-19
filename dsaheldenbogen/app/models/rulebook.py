from __future__ import annotations  # required till PEP 563

from typing import List

from dsaheldenbogen.app.models.exceptions import UnknownRulebookError
from dsaheldenbogen.app.resource import Resource

_RESOURCE_FOLDER = 'rulebook'
_ENTRYPOINT_FILE = '_entrypoint.lp'
_COMMON_FILE = 'common.lp'


class Rulebook:
    RES = Resource

    name: str

    # ## PRIVATE CONSTRUCTORS - START
    # see: https://itecnote.com/tecnote/python-private-constructor-in-python/
    __create_key = object()

    def __init__(self, name, create_key=None):
        assert (create_key == self.__create_key), "Constructor is private, call denied."
        self.name = name

    @classmethod
    def map(cls, rulebooks: List[str]) -> List[Rulebook]:
        known = [r.name for r in cls.list_known()]
        if set(rulebooks) - set(known):
            raise UnknownRulebookError(list(set(rulebooks) - set(known)))
        return [cls(r, cls.__create_key) for r in rulebooks]

    @classmethod
    def list_known(cls) -> List[Rulebook]:
        return [cls(r, cls.__create_key) for r in cls.RES.list_dirs(cls.resource_folder_name())]

    # ## PRIVATE CONSTRUCTORS - END

    def entrypoint_file(self) -> str:
        return self.RES.get_abs_path(f"{_RESOURCE_FOLDER}/{self.name}/{_ENTRYPOINT_FILE}")

    def folder(self) -> str:
        return f"{_RESOURCE_FOLDER}/{self.name}"

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    @staticmethod
    def entrypoint_file_name() -> str:
        return _ENTRYPOINT_FILE

    @staticmethod
    def resource_folder_name() -> str:
        return _RESOURCE_FOLDER

    @classmethod
    def common_file(cls) -> str:
        return cls.RES.get_abs_path(f"{_RESOURCE_FOLDER}/{_COMMON_FILE}")
