from app.models.base_enum import BaseEnum


class Feature(str, BaseEnum):
    SPECIES = 'species'
    CULTURE = 'culture'
    PROFESSION = 'profession'
    ADVANTAGE = 'advantage'
    DISADVANTAGE = 'disadvantage'
    SKILL = 'skill'
