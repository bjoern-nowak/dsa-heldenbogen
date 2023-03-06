from app.models.base_enum import BaseEnum


class Feature(str, BaseEnum):
    SPECIES = 'Species'
    CULTURE = 'Culture'
    PROFESSION = 'Profession'
    ADVANTAGE = 'Advantage'
    DISADVANTAGE = 'Disadvantage'
    SKILL = 'Skill'
