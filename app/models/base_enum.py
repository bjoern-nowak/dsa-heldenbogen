from enum import Enum


class BaseEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

    def __str__(self):
        return self.value
