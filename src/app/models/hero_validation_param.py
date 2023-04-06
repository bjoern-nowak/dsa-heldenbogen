from src.app.models.base_enum import BaseEnum


class HeroValidationParam(str, BaseEnum):
    C_F = 'caused_feature'
    C_F_LEVEL = 'caused_feature_level'
    C_F_USING = 'caused_feature_using'
    C_F_VALUE = 'caused_feature_value'
    R_F = 'referred_feature'
    R_F_LEVEL = 'referred_feature_level'
    R_F_USING = 'referred_feature_using'
    R_F_VALUE = 'referred_feature_value'
    MIN_LEVEL = 'min_level'
    SELECTION = 'selection'
    SELECTION_MIN_CHOICES = 'selection_min_choices'
    MAX_LEVEL = 'max_level'
    MAX_COUNT = 'max_count'
