from app.models.dis_advantage import DisAdvantage
from app.models.experience_level import ExperienceLevel
from app.models.hero import Hero
from app.models.skill import Skill

SOELDNER = Hero(
    name='valid_söldner',
    experience_level=ExperienceLevel.AVERAGE,
    species='Zwerg',
    culture='Ambosszwerge',
    profession='Söldner',
    talents=[
        Skill(name='Körperbeherrschung', level=3),
        Skill(name='Kraftakt', level=3),
        Skill(name='Selbstbeherrschung', level=4),
        Skill(name='Zechen', level=5),
        Skill(name='Menschenkenntnis', level=3),
        Skill(name='Überreden', level=3),
        Skill(name='Orientierung', level=4),
        Skill(name='Wildnisleben', level=3),
        Skill(name='Götter & Kulte', level=3),
        Skill(name='Kriegskunst', level=6),
        Skill(name='Sagen & Legenden', level=5),
        Skill(name='Handel', level=3),
        Skill(name='Heilkunde Wunden', level=4),
    ],
    combat_techniques=[
        Skill(name='Armbrüste', level=10),
        Skill(name='Raufen', level=10),
        Skill(name='Hiebwaffen', level=10),
    ],
    advantages=[
        DisAdvantage(name='Dunkelsicht'),
        DisAdvantage(name='Immunität', uses='Tulmadron'),
    ],
    disadvantages=[
        DisAdvantage(name='Unfähig', uses='Schwimmen'),
    ],
)

ZAUBERWEBER = Hero(
    name='valid_zauberweber',
    experience_level=ExperienceLevel.AVERAGE,
    species='Elfen',
    culture='Waldelfen',
    profession='Zauberweber',
    talents=[
        Skill(name='Körperbeherrschung', level=4),
        Skill(name='Schwimmen', level=4),
        Skill(name='Singen', level=5),
        Skill(name='Willenskraft', level=3),
        Skill(name='Fährtensuchen', level=4),
        Skill(name='Orientierung', level=3),
        Skill(name='Pflanzenkunde', level=5),
        Skill(name='Wildnisleben', level=4),
        Skill(name='Geschichtswissen', level=4),
        Skill(name='Götter & Kulte', level=4),
        Skill(name='Magiekunde', level=5),
        Skill(name='Sternkunde', level=5),
        Skill(name='Musizieren', level=7),
    ],
    combat_techniques=[],
    advantages=[],
    disadvantages=[],
)

HAENDLER = Hero(
    name='valid_händler',
    experience_level=ExperienceLevel.AVERAGE,
    species='Mensch',
    culture='Andergaster',
    profession='Händler',
    talents=[],
    combat_techniques=[],
    advantages=[],
    disadvantages=[],
)
