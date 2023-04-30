from typing import List
from typing import Optional

from dsaheldenbogen.app.engine.rulebook_function import RulebookFunction
from dsaheldenbogen.app.engine.rulebook_program import RulebookProgram
from dsaheldenbogen.app.logger import getLogger
from dsaheldenbogen.app.models.rulebook import Rulebook
from dsaheldenbogen.app.resource import Resource
from dsaheldenbogen.app.services.rulebook_executor import RulebookExecutor

logger = getLogger(__name__)


class RulebookValidator:
    """
    Validates that within a rulebook resource folder all required files are present.
    TODO It does not check if any of these files are loaded (LP: #include).
    """
    REQUIRED_PROGRAMS = [
        RulebookProgram.RULEBOOK_USABLE,
    ]

    required_files: set[str] = {Rulebook.entrypoint_file_name(), 'meta.lp', 'rules.lp'}

    @classmethod
    def filter(cls, rulebooks: List[Rulebook]) -> List[Rulebook]:
        valid_books = []
        for rulebook in rulebooks:
            errors = cls.check(rulebook)
            if errors:
                logger.warning(f"Rulebook '{rulebook}' is not valid and will be ignored.")
                logger.debug(errors)
            else:
                valid_books.append(rulebook)
        return valid_books

    @classmethod
    def check(cls, rulebook: Rulebook) -> List[str]:
        """
        :return: list of errors, rulebook is valid when empty
        """
        try:
            errors = [cls._file_structure_valid(rulebook),
                      cls._has_required_programs(rulebook)] \
                     + cls._only_declares_itself(rulebook)
            return [err for err in errors if err is not None]
        except Exception as ex:
            logger.exception(f"Could not validate rulebook '{rulebook}'.")
            raise ex

    @classmethod
    def _file_structure_valid(cls, rulebook: Rulebook) -> Optional[str]:
        found_files = set(Resource.list_files(rulebook.folder()))
        if not cls.required_files.issubset(found_files):
            return f"Rulebook '{rulebook}' missing required file(s): {cls.required_files - found_files}"

    @classmethod
    def _has_required_programs(cls, rulebook: Rulebook) -> Optional[str]:
        book = RulebookExecutor(rulebook)
        missing_programs = book.has_programs(cls.REQUIRED_PROGRAMS)
        if missing_programs:
            return f"Rulebook '{rulebook}' missing required program(s): {missing_programs}"

    @staticmethod
    def _only_declares_itself(rulebook: Rulebook) -> List[str]:
        errors = []
        book = RulebookExecutor(rulebook)
        found, others = book.has_function_with_value([RulebookProgram.RULEBOOK_USABLE],
                                                     RulebookFunction.RULEBOOK,
                                                     rulebook.name)
        if not found:
            errors.append(f"Rulebook '{rulebook}' does not declares itself as fact.")
        if others:
            errors.append(f"Rulebook '{rulebook}' declares to be other rulebook(s): {others}")
        return errors
