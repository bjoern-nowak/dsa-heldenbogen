from src.app.models.base_enum import BaseEnum


# TODO [ASK] are there expansions which adss more? then this must be dynamiclly in the LP
class Characteristic(str, BaseEnum):
    """
    TODO currently not in use
    """
    COURAGE = 'Courage'
    WISDOM = 'Wisdom'
    INTUITION = 'Intuition'
    CHARISMA = 'Charisma'
    DEXTERITY = 'Dexterity'
    AGILITY = 'Agility'
    CONSTITUTION = 'Constitution'
    BODYSTRENGTH = 'Bodystrength'
