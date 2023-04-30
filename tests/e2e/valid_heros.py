from enum import Enum
from typing import List
from typing import NamedTuple

from dsaheldenbogen.api.schemas.hero import Hero


# pylint: disable=duplicate-code

class ValidHeroTestcase(NamedTuple):
    rulebooks: List[str]
    hero: Hero


class ValidHeroTestcases(ValidHeroTestcase, Enum):

    @classmethod
    def all(cls) -> List[tuple[ValidHeroTestcase]]:
        """List all values of the enum"""
        return list(map(lambda c: (c.value,), cls))

    SOELDNER = ValidHeroTestcase(['dsa5'], Hero(
        name='valid_söldner',
        experience_level='Durchschnittlich',
        race='Zwerg',
        culture='Ambosszwerge',
        profession='Söldner',
        talents={'Körperbeherrschung': 3, 'Kraftakt': 3, 'Selbstbeherrschung': 4, 'Zechen': 5, 'Menschenkenntnis': 3,
                 'Überreden': 3, 'Orientierung': 4, 'Wildnisleben': 3, 'Götter & Kulte': 3, 'Kriegskunst': 6,
                 'Sagen & Legenden': 5, 'Handel': 3, 'Heilkunde Wunden': 4},
        combat_techniques={'Armbrüste': 10, 'Raufen': 10, 'Hiebwaffen': 10},
        advantages=[('Dunkelsicht', '', 1), ('Immunität', 'Tulmadron', 1)],
        disadvantages=[('Unfähig', 'Schwimmen', 1)],
    ))

    ZAUBERWEBER = ValidHeroTestcase(['dsa5'], Hero(
        name='valid_zauberweber',
        experience_level='Durchschnittlich',
        race='Elfen',
        culture='Waldelfen',
        profession='Zauberweber',
        talents={'Körperbeherrschung': 4, 'Schwimmen': 4, 'Singen': 5, 'Willenskraft': 3, 'Fährtensuchen': 4, 'Orientierung': 3,
                 'Pflanzenkunde': 5, 'Wildnisleben': 4, 'Geschichtswissen': 4, 'Götter & Kulte': 4, 'Magiekunde': 5,
                 'Sternkunde': 5, 'Musizieren': 7},
        combat_techniques={},
        advantages=[('Zauberer', '', 1), ('Zweistimmiger Gesang', '', 1), ('Altersresistenz', '', 1), ('Dunkelsicht', '', 1),
                    ('Nichtschläfer', '', 1)],
        disadvantages=[('Sensibler Geruchssinn', '', 1), ('Unfähig', 'Zechen', 1)],
    ))

    HAENDLER = ValidHeroTestcase(['dsa5'], Hero(
        name='valid_händler',
        experience_level='Durchschnittlich',
        race='Mensch',
        culture='Andergaster',
        profession='Händler',
        talents={},
        combat_techniques={},
        advantages=[],
        disadvantages=[],
    ))

    SKULDRUN = ValidHeroTestcase(['dsa5', 'dsa5_aventurisches_götterwirken_2'], Hero(
        name='valid_skuldrun',
        experience_level='Erfahren',
        race='Mensch',
        culture='Fjarninger',
        profession='Skuldrun',
        talents={"Körperbeherrschung": 4, "Kraftakt": 6, "Selbstbeherrschung": 4, "Sinnesschärfe": 4, "Bekehren & Überzeugen": 2,
                 "Einschüchtern": 2, "Etikette": 4, "Menschenkenntnis": 4, "Willenskraft": 4, "Orientierung": 4,
                 "Pflanzenkunde": 2, "Tierkunde": 4, "Wildnisleben": 4, "Geschichtswissen": 4, "Götter & Kulte": 5, "Rechnen": 2,
                 "Rechtskunde": 5, "Sagen & Legenden": 6, "Heilkunde Krankheiten": 4, "Heilkunde Seele": 4,
                 "Heilkunde Wunden": 3},
        combat_techniques={'Hiebwaffen': 11, 'Raufen': 10, 'Stangenwaffen': 10, 'Wurfwaffen': 8},
        advantages=[('Geweihter', '', 1)],
        disadvantages=[('Prinzipientreue', '', 1), ('Verpflichtungen', '', 2)],
    ))
