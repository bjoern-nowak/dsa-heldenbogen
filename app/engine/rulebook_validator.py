from typing import List

from app.resource import list_files
from app.service.regelwerk import Regelwerk


class RulebookValidator():
    required_files: set[str] = {"meta.lp", "base_rules.lp"}
    optional_files: set[str] = {"optional_rules.lp"}

    @staticmethod
    def filter(rulebooks: List[Regelwerk]) -> List[Regelwerk]:
        valid_books = []
        for book in rulebooks:
            if RulebookValidator.check(book):
                valid_books.append(book)
            else:
                print(f"Rulebook {book} is not valid and will be ignored.")
        return valid_books

    @staticmethod
    def check(rulebook: Regelwerk) -> bool:
        # print(f"check {rulebook}")
        found_files = set(list_files(f"regelwerk/{rulebook.value}"))
        # print(f"found: {found_files}")
        if not RulebookValidator.required_files.issubset(found_files):
            return False
        return True
