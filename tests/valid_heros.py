from dsaheldenbogen.app.models.dis_advantage import DisAdvantage
from dsaheldenbogen.app.models.hero import Hero
from dsaheldenbogen.app.models.skill import Skill

SOELDNER = Hero(
    name='valid_söldner',
    experience_level='Average',
    race='Zwerg',
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

ZAUBERWEBER = Hero(
    name='valid_zauberweber',
    experience_level='Average',
    race='Elfen',
    culture='Waldelfen',
    profession='Zauberweber',
    talents=Skill.list_by([('Körperbeherrschung', 4), ('Schwimmen', 4), ('Singen', 5), ('Willenskraft', 3), ('Fährtensuchen', 4),
                           ('Orientierung', 3), ('Pflanzenkunde', 5), ('Wildnisleben', 4), ('Geschichtswissen', 4),
                           ('Götter & Kulte', 4), ('Magiekunde', 5), ('Sternkunde', 5), ('Musizieren', 7)]),
    combat_techniques=[],
    advantages=DisAdvantage.list_by([('Zauberer',), ('Zweistimmiger Gesang',), ('Altersresistenz',), ('Dunkelsicht',),
                                     ('Nichtschläfer',)]),
    disadvantages=DisAdvantage.list_by([('Sensibler Geruchssinn',), ('Unfähig', 'Zechen')]),
)

HAENDLER = Hero(
    name='valid_händler',
    experience_level='Average',
    race='Mensch',
    culture='Andergaster',
    profession='Händler',
    talents=[],
    combat_techniques=[],
    advantages=[],
    disadvantages=[],
)
