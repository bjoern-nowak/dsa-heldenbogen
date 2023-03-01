from typing import List

from app.models.rulebook import Rulebook
from app.resource import list_files


class RulebookValidator():
    required_files: set[str] = {"meta.lp", "rules.lp"}
    optional_files: set[str] = {"rules_optional.lp"}

    @staticmethod
    def filter(rulebooks: List[Rulebook]) -> List[Rulebook]:
        valid_books = []
        for book in rulebooks:
            if RulebookValidator._check(book):
                valid_books.append(book)
            else:
                print(f"Rulebook {book} is not valid and will be ignored.")
        return valid_books

    @staticmethod
    def _check(rulebook: Rulebook) -> bool:
        return RulebookValidator._files_valid(rulebook)

    @staticmethod
    def _files_valid(rulebook: Rulebook) -> bool:
        # print(f"check {rulebook}")
        found_files = set(list_files(f"regelwerk/{rulebook}"))
        # print(f"found: {found_files}")
        if not RulebookValidator.required_files.issubset(found_files):
            return False
        return True
