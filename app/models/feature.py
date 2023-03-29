from app.models.base_enum import BaseEnum


class Feature(str, BaseEnum):
    """Represents relevant heros/characters fields/features"""
    EXPERIENCE_LEVEL = 'experience_level'
    RACE = 'race'
    CULTURE = 'culture'
    PROFESSION = 'profession'
    ADVANTAGE = 'advantage'
    DISADVANTAGE = 'disadvantage'
    TALENT = 'talent'
    COMBAT_TECHNIQUE = 'combat_technique'
