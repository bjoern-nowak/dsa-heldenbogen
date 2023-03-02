from enum import Enum


# TODO [ASK] are there expansions which adss more?
#  then this must be dynamiclly in the LP
class Characteristic(str, Enum):
    COURAGE = 'Courage'
    WISDOM = 'Wisdom'
    INTUITION = 'Intuition'
    CHARISMA = 'Charisma'
    DEXTERITY = 'Dexterity'
    AGILITY = 'Agility'
    CONSTITUTION = 'Constitution'
    BODYSTRENGTH = 'Bodystrength'
