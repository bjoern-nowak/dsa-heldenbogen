from app.models.base_enum import BaseEnum


class Feature(str, BaseEnum):
    EXPERIENCE_LEVEL = 'experience_level'
    SPECIES = 'species'
    CULTURE = 'culture'
    PROFESSION = 'profession'
    ADVANTAGE = 'advantage'
    DISADVANTAGE = 'disadvantage'
    SKILL = 'skill'
