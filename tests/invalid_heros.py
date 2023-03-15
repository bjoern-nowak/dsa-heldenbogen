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
        talents=Skill.list_by([('Körperbeherrschung', 3), ('Kraftakt', 3), ('Selbstbeherrschung', 4), ('Zechen', 5),
                               ('Menschenkenntnis', 3), ('Überreden', 3), ('Orientierung', 4), ('Wildnisleben', 3),
                               ('Götter & Kulte', 3), ('Kriegskunst', 6), ('Sagen & Legenden', 5), ('Handel', 3),
                               ('Heilkunde Wunden', 4)]),
        combat_techniques=Skill.list_by([('Armbrüste', 10), ('Raufen', 10), ('Hiebwaffen', 10)]),
        advantages=DisAdvantage.list_by([('Dunkelsicht',), ('Immunität', 'Tulmadron')]),
        disadvantages=DisAdvantage.list_by([('Unfähig', 'Schwimmen')]),
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
        talents=Skill.list_by([('Körperbeherrschung', 3), ('Kraftakt', 3), ('Selbstbeherrschung', 4), ('Zechen', 5),
                               ('Menschenkenntnis', 3), ('Überreden', 3), ('Orientierung', 4), ('Wildnisleben', 3),
                               ('Götter & Kulte', 3), ('Kriegskunst', 6), ('Sagen & Legenden', 5), ('Handel', 3),
                               ('Heilkunde Wunden', 4)]),
        combat_techniques=Skill.list_by([('Armbrüste', 10), ('Raufen', 10), ('Hiebwaffen', 10)]),
        advantages=DisAdvantage.list_by([('Dunkelsicht',), ('Immunität', 'Tulmadron')]),
        disadvantages=DisAdvantage.list_by([('Unfähig', 'Schwimmen')]),
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
        talents=Skill.list_by([('Körperbeherrschung', 3), ('Kraftakt', 3), ('Selbstbeherrschung', 4), ('Zechen', 5),
                               ('Menschenkenntnis', 3), ('Überreden', 3), ('Orientierung', 4), ('Wildnisleben', 3),
                               ('Götter & Kulte', 3), ('Kriegskunst', 6), ('Sagen & Legenden', 5), ('Handel', 3),
                               ('Heilkunde Wunden', 4)]),
        combat_techniques=Skill.list_by([('Armbrüste', 10), ('Raufen', 10), ('Hiebwaffen', 10)]),
        advantages=DisAdvantage.list_by([('Dunkelsicht',), ('Immunität', 'Tulmadron')]),
        disadvantages=DisAdvantage.list_by([('Unfähig', 'Schwimmen')]),
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
        talents=Skill.list_by([('__unknown__', 1),
                               ('Körperbeherrschung', 3), ('Kraftakt', 3), ('Selbstbeherrschung', 4), ('Zechen', 5),
                               ('Menschenkenntnis', 3), ('Überreden', 3), ('Orientierung', 4), ('Wildnisleben', 3),
                               ('Götter & Kulte', 3), ('Kriegskunst', 6), ('Sagen & Legenden', 5), ('Handel', 3),
                               ('Heilkunde Wunden', 4)]),
        combat_techniques=Skill.list_by([('Armbrüste', 10), ('Raufen', 10), ('Hiebwaffen', 10)]),
        advantages=DisAdvantage.list_by([('Dunkelsicht',), ('Immunität', 'Tulmadron')]),
        disadvantages=DisAdvantage.list_by([('Unfähig', 'Schwimmen')]),
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
        talents=Skill.list_by([('Körperbeherrschung', 3), ('Kraftakt', 3), ('Selbstbeherrschung', 4), ('Zechen', 5),
                               ('Menschenkenntnis', 3), ('Überreden', 3), ('Orientierung', 4), ('Wildnisleben', 3),
                               ('Götter & Kulte', 3), ('Kriegskunst', 6), ('Sagen & Legenden', 5), ('Handel', 3),
                               ('Heilkunde Wunden', 4)]),
        combat_techniques=Skill.list_by([('__unknown__', 1), ('Armbrüste', 10), ('Raufen', 10), ('Hiebwaffen', 10)]),
        advantages=DisAdvantage.list_by([('Dunkelsicht',), ('Immunität', 'Tulmadron')]),
        disadvantages=DisAdvantage.list_by([('Unfähig', 'Schwimmen')]),
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
        talents=Skill.list_by([('Körperbeherrschung', 3), ('Kraftakt', 3), ('Selbstbeherrschung', 4), ('Zechen', 5),
                               ('Menschenkenntnis', 3), ('Überreden', 3), ('Orientierung', 4), ('Wildnisleben', 3),
                               ('Götter & Kulte', 3), ('Kriegskunst', 6), ('Sagen & Legenden', 5), ('Handel', 3),
                               ('Heilkunde Wunden', 4)]),
        combat_techniques=Skill.list_by([('Armbrüste', 10), ('Raufen', 10), ('Hiebwaffen', 10)]),
        advantages=DisAdvantage.list_by([('__unknown__',), ('Dunkelsicht',), ('Immunität', 'Tulmadron')]),
        disadvantages=DisAdvantage.list_by([('Unfähig', 'Schwimmen')]),
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
        talents=Skill.list_by([('Körperbeherrschung', 3), ('Kraftakt', 3), ('Selbstbeherrschung', 4), ('Zechen', 5),
                               ('Menschenkenntnis', 3), ('Überreden', 3), ('Orientierung', 4), ('Wildnisleben', 3),
                               ('Götter & Kulte', 3), ('Kriegskunst', 6), ('Sagen & Legenden', 5), ('Handel', 3),
                               ('Heilkunde Wunden', 4)]),
        combat_techniques=Skill.list_by([('Armbrüste', 10), ('Raufen', 10), ('Hiebwaffen', 10)]),
        advantages=DisAdvantage.list_by([('Dunkelsicht',), ('Immunität', 'Tulmadron')]),
        disadvantages=DisAdvantage.list_by([('__unknown__',), ('Unfähig', 'Schwimmen')]),
    )
)
