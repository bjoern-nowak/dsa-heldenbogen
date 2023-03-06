from app.models.base_enum import BaseEnum


# TODO to be used
class Basevalue(str, BaseEnum):
    LIFEENERGY = 'Lifeenergy'
    ASTRALENERGY = 'Astralenergy'
    CARMAENERGY = 'Carmaenergy'
    SOULPOWER = 'Soulpower'
    TOUGHNESS = 'Toughness'
    EVASION = 'Evasion'
    INITIATIVE = 'Initiative'
    SPEED = 'Speed'
