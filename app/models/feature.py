from enum import Enum


class Feature(str, Enum):
    Spezies = 'Spezies'
    Kultur = 'Kultur'
    Profession = 'Profession'
    Vorteil = 'Vorteil'
    Nachteil = 'Nachteil'
    Fertigkeit = 'Fertigkeit'
