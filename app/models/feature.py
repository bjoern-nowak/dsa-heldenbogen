from enum import Enum


class Feature(str, Enum):
    SPECIES = 'Species'
    CULTURE = 'Culture'
    PROFESSION = 'Profession'
    ADVANTAGE = 'Advantage'
    DISADVANTAGE = 'Disadvantage'
    SKILL = 'Skill'

    def __str__(self):
        return self.value
