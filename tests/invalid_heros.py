from enum import Enum
from typing import List
from typing import NamedTuple
from typing import Optional

from dsaheldenbogen.app.models.dis_advantage import DisAdvantage
from dsaheldenbogen.app.models.hero import Hero
from dsaheldenbogen.app.models.hero_validation_error import HeroValidationError
from dsaheldenbogen.app.models.hero_validation_param import HeroValidationParam
from dsaheldenbogen.app.models.skill import Skill


class InvalidHeroTestcase(NamedTuple):
    # expected:
    error_type: HeroValidationError.Type
    error_params: dict[HeroValidationParam, str, Optional[List[str]]]
    # given:
    rulebooks: List[str]
    hero: Hero


class InvalidHeroTestcases(InvalidHeroTestcase, Enum):

    @classmethod
    def all(cls) -> List[tuple[InvalidHeroTestcase]]:
        """List all values of the enum"""
        return list(map(lambda c: (c.value,), cls))

    UNKNOWN_RACE = InvalidHeroTestcase(
        HeroValidationError.Type.UNKNOWN,
        {
            HeroValidationParam.C_F: 'race',
            HeroValidationParam.C_F_VALUE: '__unknown__',
        },
        ['dsa5'],
        Hero(
            name='valid_söldner',
            experience_level='Average',
            race='__unknown__',
            culture='Ambosszwerge',
            profession='Söldner',
            talents=[],
            combat_techniques=[],
            advantages=[],
            disadvantages=[],
        )
    )

    UNKNOWN_CULTURE = InvalidHeroTestcase(
        HeroValidationError.Type.UNKNOWN,
        {
            HeroValidationParam.C_F: 'culture',
            HeroValidationParam.C_F_VALUE: '__unknown__',
        },
        ['dsa5'],
        Hero(
            name='valid_söldner',
            experience_level='Average',
            race='Zwerg',
            culture='__unknown__',
            profession='Söldner',
            talents=[],
            combat_techniques=[],
            advantages=[],
            disadvantages=[],
        )
    )

    UNKNOWN_PROFESSION = InvalidHeroTestcase(
        HeroValidationError.Type.UNKNOWN,
        {
            HeroValidationParam.C_F: 'profession',
            HeroValidationParam.C_F_VALUE: '__unknown__',
        },
        ['dsa5'],
        Hero(
            name='valid_söldner',
            experience_level='Average',
            race='Zwerg',
            culture='Ambosszwerge',
            profession='__unknown__',
            talents=[],
            combat_techniques=[],
            advantages=[],
            disadvantages=[],
        )
    )

    UNKNOWN_TALENT = InvalidHeroTestcase(
        HeroValidationError.Type.UNKNOWN,
        {
            HeroValidationParam.C_F: 'talent',
            HeroValidationParam.C_F_VALUE: '__unknown__',
        },
        ['dsa5'],
        Hero(
            name='valid_söldner',
            experience_level='Average',
            race='Zwerg',
            culture='Ambosszwerge',
            profession='Söldner',
            talents=[Skill(name='__unknown__')],
            combat_techniques=[],
            advantages=[],
            disadvantages=[],
        )
    )

    UNKNOWN_COMBAT_TECHNIQUE = InvalidHeroTestcase(
        HeroValidationError.Type.UNKNOWN,
        {
            HeroValidationParam.C_F: 'combat_technique',
            HeroValidationParam.C_F_VALUE: '__unknown__',
        },
        ['dsa5'],
        Hero(
            name='valid_söldner',
            experience_level='Average',
            race='Zwerg',
            culture='Ambosszwerge',
            profession='Söldner',
            talents=[],
            combat_techniques=[Skill(name='__unknown__')],
            advantages=[],
            disadvantages=[],
        )
    )

    UNKNOWN_ADVANTAGE = InvalidHeroTestcase(
        HeroValidationError.Type.UNKNOWN,
        {
            HeroValidationParam.C_F: 'advantage',
            HeroValidationParam.C_F_VALUE: '__unknown__',
        },
        ['dsa5'],
        Hero(
            name='valid_söldner',
            experience_level='Average',
            race='Zwerg',
            culture='Ambosszwerge',
            profession='Söldner',
            talents=[],
            combat_techniques=[],
            advantages=[DisAdvantage(name='__unknown__')],
            disadvantages=[],
        )
    )

    UNKNOWN_DISADVANTAGE = InvalidHeroTestcase(
        HeroValidationError.Type.UNKNOWN,
        {
            HeroValidationParam.C_F: 'disadvantage',
            HeroValidationParam.C_F_VALUE: '__unknown__',
        },
        ['dsa5'],
        Hero(
            name='valid_söldner',
            experience_level='Average',
            race='Zwerg',
            culture='Ambosszwerge',
            profession='Söldner',
            talents=[],
            combat_techniques=[],
            advantages=[],
            disadvantages=[DisAdvantage(name='__unknown__')],
        )
    )

    CULTURE_UNUSABLE_BY_RACE = InvalidHeroTestcase(
        HeroValidationError.Type.UNUSABLE_BY,
        {
            HeroValidationParam.C_F: 'culture',
            HeroValidationParam.C_F_VALUE: 'Andergaster',
            HeroValidationParam.R_F: 'race',
            HeroValidationParam.R_F_VALUE: 'Zwerg',
        },
        ['dsa5'],
        Hero(
            name='valid_söldner',
            experience_level='Average',
            race='Zwerg',
            culture='Andergaster',
            profession='Söldner',
            talents=[],
            combat_techniques=[],
            advantages=[],
            disadvantages=[],
        )
    )

    PROFESSION_UNUSABLE_BY_RACE = InvalidHeroTestcase(
        HeroValidationError.Type.UNUSABLE_BY,
        {
            HeroValidationParam.C_F: 'profession',
            HeroValidationParam.C_F_VALUE: 'Zauberweber',
            HeroValidationParam.R_F: 'race',
            HeroValidationParam.R_F_VALUE: 'Zwerg',
        },
        ['dsa5'],
        Hero(
            name='valid_söldner',
            experience_level='Average',
            race='Zwerg',
            culture='Ambosszwerge',
            profession='Zauberweber',
            talents=[],
            combat_techniques=[],
            advantages=[],
            disadvantages=[],
        )
    )

    PROFESSION_UNUSABLE_BY_CULTURE = InvalidHeroTestcase(
        HeroValidationError.Type.UNUSABLE_BY,
        {
            HeroValidationParam.C_F: 'profession',
            HeroValidationParam.C_F_VALUE: 'Skuldrun',
            HeroValidationParam.R_F: 'culture',
            HeroValidationParam.R_F_VALUE: 'Ambosszwerge',
        },
        ['dsa5', 'dsa5_aventurisches_götterwirken_2'],
        Hero(
            name='valid_söldner',
            experience_level='Average',
            race='Zwerg',
            culture='Ambosszwerge',
            profession='Skuldrun',
            talents=[],
            combat_techniques=[],
            advantages=[],
            disadvantages=[],
        )
    )

    PROFESSION_MISSING_LEVEL_FOR_TALENT = InvalidHeroTestcase(
        HeroValidationError.Type.MISSING_LEVEL,
        {
            HeroValidationParam.C_F: 'profession',
            HeroValidationParam.C_F_VALUE: 'Söldner',
            HeroValidationParam.R_F: 'talent',
            HeroValidationParam.R_F_VALUE: 'Körperbeherrschung',
            HeroValidationParam.MIN_LEVEL: 3,
        },
        ['dsa5'],
        Hero(
            name='valid_söldner',
            experience_level='Average',
            race='Zwerg',
            culture='Ambosszwerge',
            profession='Söldner',
            talents=[],
            combat_techniques=[],
            advantages=[],
            disadvantages=[],
        )
    )

    PROFESSION_MISSING_LEVEL_FOR_COMBAT_TECHNIQUE = InvalidHeroTestcase(
        HeroValidationError.Type.MISSING_LEVEL,
        {
            HeroValidationParam.C_F: 'profession',
            HeroValidationParam.C_F_VALUE: 'Söldner',
            HeroValidationParam.R_F: 'combat_technique',
            HeroValidationParam.R_F_VALUE: 'Armbrüste',
            HeroValidationParam.MIN_LEVEL: 10,
        },
        ['dsa5'],
        Hero(
            name='valid_söldner',
            experience_level='Average',
            race='Zwerg',
            culture='Ambosszwerge',
            profession='Söldner',
            talents=[],
            combat_techniques=[],
            advantages=[],
            disadvantages=[],
        )
    )

    PROFESSION_MISSING_LEVEL_FOR_ANY_OF_COMBAT_TECHNIQUES = InvalidHeroTestcase(
        HeroValidationError.Type.MISSING_LEVEL,
        {
            HeroValidationParam.C_F: 'profession',
            HeroValidationParam.C_F_VALUE: 'Söldner',
            HeroValidationParam.R_F: 'combat_technique',
            HeroValidationParam.SELECTION: ['Hiebwaffen', 'Schwerter', 'Stangenwaffen', 'Zweihandschwerter',
                                            'Zweihandhiebwaffen'],
            HeroValidationParam.MIN_LEVEL: 10,
            HeroValidationParam.SELECTION_MIN_CHOICES: 1,
        },
        ['dsa5'],
        Hero(
            name='valid_söldner',
            experience_level='Average',
            race='Zwerg',
            culture='Ambosszwerge',
            profession='Söldner',
            talents=[],
            combat_techniques=[],
            advantages=[],
            disadvantages=[],
        )
    )

    TALENT_EXCEEDS_MAX_LEVEL_BY_EXPERIENCE = InvalidHeroTestcase(
        HeroValidationError.Type.MAX_LVL_EXCEEDED,
        {
            HeroValidationParam.C_F: 'talent',
            HeroValidationParam.C_F_VALUE: 'Körperbeherrschung',
            HeroValidationParam.C_F_LEVEL: 17,
            HeroValidationParam.MAX_LEVEL: 16,
        },
        ['dsa5'],
        Hero(
            name='valid_söldner',
            experience_level='Masterful',
            race='Zwerg',
            culture='Ambosszwerge',
            profession='Söldner',
            talents=Skill.list_by([('Körperbeherrschung', 17), ('Kraftakt', 3), ('Selbstbeherrschung', 4), ('Zechen', 5),
                                   ('Menschenkenntnis', 3), ('Überreden', 3), ('Orientierung', 4), ('Wildnisleben', 3),
                                   ('Götter & Kulte', 3), ('Kriegskunst', 6), ('Sagen & Legenden', 5), ('Handel', 3),
                                   ('Heilkunde Wunden', 4)]),
            combat_techniques=Skill.list_by([('Armbrüste', 10), ('Raufen', 10), ('Hiebwaffen', 10)]),
            advantages=DisAdvantage.list_by([('Dunkelsicht',), ('Immunität', 'Tulmadron')]),
            disadvantages=DisAdvantage.list_by([('Unfähig', 'Schwimmen')]),
        )
    )

    COMBAT_TECHNIQUE_EXCEEDS_MAX_LEVEL_BY_EXPERIENCE = InvalidHeroTestcase(
        HeroValidationError.Type.MAX_LVL_EXCEEDED,
        {
            HeroValidationParam.C_F: 'combat_technique',
            HeroValidationParam.C_F_VALUE: 'Armbrüste',
            HeroValidationParam.C_F_LEVEL: 17,
            HeroValidationParam.MAX_LEVEL: 16,
        },
        ['dsa5'],
        Hero(
            name='valid_söldner',
            experience_level='Masterful',
            race='Zwerg',
            culture='Ambosszwerge',
            profession='Söldner',
            talents=Skill.list_by([('Körperbeherrschung', 3), ('Kraftakt', 3), ('Selbstbeherrschung', 4), ('Zechen', 5),
                                   ('Menschenkenntnis', 3), ('Überreden', 3), ('Orientierung', 4), ('Wildnisleben', 3),
                                   ('Götter & Kulte', 3), ('Kriegskunst', 6), ('Sagen & Legenden', 5), ('Handel', 3),
                                   ('Heilkunde Wunden', 4)]),
            combat_techniques=Skill.list_by([('Armbrüste', 17), ('Raufen', 10), ('Hiebwaffen', 10)]),
            advantages=DisAdvantage.list_by([('Dunkelsicht',), ('Immunität', 'Tulmadron')]),
            disadvantages=DisAdvantage.list_by([('Unfähig', 'Schwimmen')]),
        )
    )
