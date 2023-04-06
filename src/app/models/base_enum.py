from enum import Enum


class BaseEnum(Enum):

    @classmethod
    def list(cls):
        """List all values of the enum"""
        return list(map(lambda c: c.value, cls))

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value
