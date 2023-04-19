import logging
from typing import List

from dsaheldenbogen.app.models.rulebook import Rulebook
from dsaheldenbogen.app.resource import Resource

logger = logging.getLogger(__name__)


class RulebookValidator:
    """
    Validates that within a rulebook resource folder all required files are present.
    TODO It does not check if any of these files are loaded (LP: #include).
    """
    required_files: set[str] = {Rulebook.entrypoint_file_name(), 'meta.lp', 'rules.lp'}

    @staticmethod
    def filter(rulebooks: List[Rulebook]) -> List[Rulebook]:
        valid_books = []
        for book in rulebooks:
            if RulebookValidator._check(book):
                valid_books.append(book)
            else:
                logger.error(f"Rulebook '{book}' is not valid and will be ignored.")
        return valid_books

    @staticmethod
    def _check(rulebook: Rulebook) -> bool:
        return RulebookValidator._files_valid(rulebook)

    @staticmethod
    def _files_valid(rulebook: Rulebook) -> bool:
        try:
            found_files = set(Resource.list_files(rulebook.folder()))
            if not RulebookValidator.required_files.issubset(found_files):
                return False
            return True
        except Exception:
            logger.exception(f"Could not validate '{rulebook}' rulebook files.")
            return False
