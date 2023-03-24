from app.models.base_enum import BaseEnum


class Basevalue(str, BaseEnum):
    """
    TODO currently not in use
    """
    LIFEENERGY = 'Lifeenergy'
    ASTRALENERGY = 'Astralenergy'
    CARMAENERGY = 'Carmaenergy'
    SOULPOWER = 'Soulpower'
    TOUGHNESS = 'Toughness'
    EVASION = 'Evasion'
    INITIATIVE = 'Initiative'
    SPEED = 'Speed'
