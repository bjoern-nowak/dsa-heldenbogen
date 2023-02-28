from enum import Enum


class Rulebook(str, Enum):
    DSA5 = 'dsa5'
    DSA5_EXPANSION = 'dsa5_expansion'

    def __str__(self):
        return self.value
