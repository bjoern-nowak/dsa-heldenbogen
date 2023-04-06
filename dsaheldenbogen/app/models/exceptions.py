from typing import List


# TODO should this be in model module/package?


class UnknownRulebookError(Exception):
    def __init__(self, rulebooks: List[str]):
        super().__init__(f"Following requested rulebooks are unknown: {rulebooks}")
        self.rulebooks = rulebooks
