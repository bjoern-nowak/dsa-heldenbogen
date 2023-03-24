from __future__ import annotations  # required till PEP 563

from typing import List

from app import resource
from app.models.base_model import BaseModel

_RESOURCE_FOLDER = 'rulebook'
_ENTRYPOINT_FILE = '_entrypoint.lp'
_COMMON_FILE = 'common.lp'


class Rulebook(BaseModel):
    name: str

    def entrypoint_file(self) -> str:
        return resource.get_abs_path(f"{_RESOURCE_FOLDER}/{self.name}/{_ENTRYPOINT_FILE}")

    def folder(self) -> str:
        return f"{_RESOURCE_FOLDER}/{self.name}"

    @staticmethod
    def entrypoint_file_name() -> str:
        return _ENTRYPOINT_FILE

    @staticmethod
    def resource_folder_name() -> str:
        return _RESOURCE_FOLDER

    @staticmethod
    def common_file() -> str:
        return resource.get_abs_path(f"{_RESOURCE_FOLDER}/{_COMMON_FILE}")

    @staticmethod
    def map(rulebooks: List[str]) -> List[Rulebook]:
        known = [r.name for r in Rulebook.list_known()]
        if set(rulebooks) - set(known):
            raise UnknownRulebookError(rulebooks)
        return [Rulebook(name=r) for r in rulebooks]

    @staticmethod
    def list_known() -> List[Rulebook]:
        return [Rulebook(name=r) for r in resource.list_dirs(Rulebook.res_folder_name())]

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class UnknownRulebookError(Exception):
    def __init__(self, rulebooks: List[str]):
        super().__init__(f"Following requested rulebooks are unknown: {rulebooks}")
        self.rulebooks = rulebooks
