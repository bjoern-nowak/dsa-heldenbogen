from enum import Enum


class Feature(str, Enum):
    SPEZIES = 'Spezies'
    CULTURE = 'Kultur'
    PROFESSION = 'Profession'
    VORTEIL = 'Vorteil'
    NACHTEIL = 'Nachteil'
    FERTIGKEIT = 'Fertigkeit'

    def __str__(self):
        return self.value
