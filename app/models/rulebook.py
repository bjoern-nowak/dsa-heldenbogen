from app.models.base_enum import BaseEnum
from app.resource import get_abs_path

_RULEBOOK_RES_FOLDER = 'rulebook'
_RULEBOOK_ENTRYPOINT = '_entrypoint.lp'
_COMMON_FILE = 'common.lp'


class Rulebook(str, BaseEnum):
    DSA5 = 'dsa5'
    DSA5_AVENTURISCHES_KOMPENDIUM_2 = 'dsa5_aventurisches_kompendium_2'
    DSA5_AVENTURISCHES_GOETTERWIRKEN_2 = 'dsa5_aventurisches_götterwirken_2'
    DSA5_EXTENSION_EXAMPLE = 'dsa5_extension_example'

    def entrypoint(self) -> str:
        return get_abs_path(f"{_RULEBOOK_RES_FOLDER}/{self.value}/{_RULEBOOK_ENTRYPOINT}")

    @staticmethod
    def res_folder_name() -> str:
        return _RULEBOOK_RES_FOLDER

    @staticmethod
    def entrypoint_name() -> str:
        return _RULEBOOK_ENTRYPOINT

    @staticmethod
    def common_file_name() -> str:
        return _COMMON_FILE

    @staticmethod
    def common_file() -> str:
        return get_abs_path(f"{_RULEBOOK_RES_FOLDER}/{_COMMON_FILE}")
