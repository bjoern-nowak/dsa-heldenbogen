from __future__ import annotations  # required till PEP 563

from typing import List

from app.models.base_model import BaseModel
from app.resource import get_abs_path

_RULEBOOK_RES_FOLDER = 'rulebook'
_RULEBOOK_ENTRYPOINT = '_entrypoint.lp'
_COMMON_FILE = 'common.lp'


class Rulebook(BaseModel):
    name: str

    def entrypoint(self) -> str:
        return get_abs_path(f"{_RULEBOOK_RES_FOLDER}/{self.name}/{_RULEBOOK_ENTRYPOINT}")

    @staticmethod
    def res_folder_name() -> str:
        return _RULEBOOK_RES_FOLDER

    def res_folder(self) -> str:
        return f"{_RULEBOOK_RES_FOLDER}/{self.name}"

    @staticmethod
    def entrypoint_name() -> str:
        return _RULEBOOK_ENTRYPOINT

    @staticmethod
    def common_file_name() -> str:
        return _COMMON_FILE

    @staticmethod
    def common_file() -> str:
        return get_abs_path(f"{_RULEBOOK_RES_FOLDER}/{_COMMON_FILE}")

    @staticmethod
    def list_by(rulebooks: List[str]) -> List[Rulebook]:
        return [Rulebook(name=r) for r in rulebooks]
