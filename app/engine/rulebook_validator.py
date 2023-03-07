import logging
from typing import List

from app.models import Rulebook
from app.resource import list_files

logger = logging.getLogger(__name__)


class RulebookValidator:
    """
    Validates that a rulebook resource folder has specific files.
    It does not check if any of these files are loaded.
    Only entrypoint will be loaded by the engine
    """
    required_files: set[str] = {Rulebook.entrypoint_name(), 'meta.lp', 'rules.lp'}

    @staticmethod
    def filter(rulebooks: List[Rulebook]) -> List[Rulebook]:
        valid_books = []
        for book in rulebooks:
            if RulebookValidator._check(book):
                valid_books.append(book)
            else:
                # TODO make it a warning and build a testcase for it, this shall not be thrown at runtime
                logger.warning(f"Rulebook '{book}' is not valid and will be ignored.")
        return valid_books

    @staticmethod
    def _check(rulebook: Rulebook) -> bool:
        return RulebookValidator._files_valid(rulebook)

    @staticmethod
    def _files_valid(rulebook: Rulebook) -> bool:
        found_files = set(list_files(f"{Rulebook.res_folder_name()}/{rulebook}"))
        if not RulebookValidator.required_files.issubset(found_files):
            return False
        return True
