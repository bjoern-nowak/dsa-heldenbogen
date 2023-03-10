from app.models.base_enum import BaseEnum


class ExperienceLevel(str, BaseEnum):
    INEXPERIENCED = 'Inexperienced'
    AVERAGE = 'Average'
    EXPERIENCED = 'Experienced'
    COMPETENT = 'Competent'
    MASTERFUL = 'Masterful'
    BRILLIANT = 'Brilliant'
    LEGENDARY = 'Legendary'
