from app.models.dis_advantage import DisAdvantage
from app.models.experience_level import ExperienceLevel
from app.models.hero import Hero
from app.models.hero_validation_error import HeroValidationError
from app.models.hero_validation_param import HeroValidationParam
from app.models.skill import Skill

UNKNOWN_SPECIES = (
    HeroValidationError.Type.UNKNOWN,
    {
        HeroValidationParam.C_F: 'species',
        HeroValidationParam.C_F_VALUE: '__unknown__',
    },
    Hero(
        name='valid_söldner',
        experience_level=ExperienceLevel.AVERAGE,
        species='__unknown__',
        culture='Ambosszwerge',
        profession='Söldner',
        talents=[],
        combat_techniques=[],
        advantages=[],
        disadvantages=[],
    )
)

UNKNOWN_CULTURE = (
    HeroValidationError.Type.UNKNOWN,
    {
        HeroValidationParam.C_F: 'culture',
        HeroValidationParam.C_F_VALUE: '__unknown__',
    },
    Hero(
        name='valid_söldner',
        experience_level=ExperienceLevel.AVERAGE,
        species='Zwerg',
        culture='__unknown__',
        profession='Söldner',
        talents=[],
        combat_techniques=[],
        advantages=[],
        disadvantages=[],
    )
)

UNKNOWN_PROFESSION = (
    HeroValidationError.Type.UNKNOWN,
    {
        HeroValidationParam.C_F: 'profession',
        HeroValidationParam.C_F_VALUE: '__unknown__',
    },
    Hero(
        name='valid_söldner',
        experience_level=ExperienceLevel.AVERAGE,
        species='Zwerg',
        culture='Ambosszwerge',
        profession='__unknown__',
        talents=[],
        combat_techniques=[],
        advantages=[],
        disadvantages=[],
    )
)

UNKNOWN_TALENT = (
    HeroValidationError.Type.UNKNOWN,
    {
        HeroValidationParam.C_F: 'talent',
        HeroValidationParam.C_F_VALUE: '__unknown__',
    },
    Hero(
        name='valid_söldner',
        experience_level=ExperienceLevel.AVERAGE,
        species='Zwerg',
        culture='Ambosszwerge',
        profession='Söldner',
        talents=[Skill(name='__unknown__')],
        combat_techniques=[],
        advantages=[],
        disadvantages=[],
    )
)

UNKNOWN_COMBAT_TECHNIQUE = (
    HeroValidationError.Type.UNKNOWN,
    {
        HeroValidationParam.C_F: 'combat_technique',
        HeroValidationParam.C_F_VALUE: '__unknown__',
    },
    Hero(
        name='valid_söldner',
        experience_level=ExperienceLevel.AVERAGE,
        species='Zwerg',
        culture='Ambosszwerge',
        profession='Söldner',
        talents=[],
        combat_techniques=[Skill(name='__unknown__')],
        advantages=[],
        disadvantages=[],
    )
)

UNKNOWN_ADVANTAGE = (
    HeroValidationError.Type.UNKNOWN,
    {
        HeroValidationParam.C_F: 'advantage',
        HeroValidationParam.C_F_VALUE: '__unknown__',
    },
    Hero(
        name='valid_söldner',
        experience_level=ExperienceLevel.AVERAGE,
        species='Zwerg',
        culture='Ambosszwerge',
        profession='Söldner',
        talents=[],
        combat_techniques=[],
        advantages=[DisAdvantage(name='__unknown__')],
        disadvantages=[],
    )
)

UNKNOWN_DISADVANTAGE = (
    HeroValidationError.Type.UNKNOWN,
    {
        HeroValidationParam.C_F: 'disadvantage',
        HeroValidationParam.C_F_VALUE: '__unknown__',
    },
    Hero(
        name='valid_söldner',
        experience_level=ExperienceLevel.AVERAGE,
        species='Zwerg',
        culture='Ambosszwerge',
        profession='Söldner',
        talents=[],
        combat_techniques=[],
        advantages=[],
        disadvantages=[DisAdvantage(name='__unknown__')],
    )
)
