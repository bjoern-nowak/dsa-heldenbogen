from __future__ import annotations  # required till PEP 563

from typing import List

from app import resource
from app.models.base_model import BaseModel

_RULEBOOK_RES_FOLDER = 'rulebook'
_RULEBOOK_ENTRYPOINT = '_entrypoint.lp'
_COMMON_FILE = 'common.lp'


class Rulebook(BaseModel):
    name: str

    def entrypoint(self) -> str:
        return resource.get_abs_path(f"{_RULEBOOK_RES_FOLDER}/{self.name}/{_RULEBOOK_ENTRYPOINT}")

    def res_folder(self) -> str:
        return f"{_RULEBOOK_RES_FOLDER}/{self.name}"

    @staticmethod
    def entrypoint_name() -> str:
        return _RULEBOOK_ENTRYPOINT

    @staticmethod
    def res_folder_name() -> str:
        return _RULEBOOK_RES_FOLDER

    @staticmethod
    def common_file_name() -> str:
        return _COMMON_FILE

    @staticmethod
    def common_file() -> str:
        return resource.get_abs_path(f"{_RULEBOOK_RES_FOLDER}/{_COMMON_FILE}")

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
