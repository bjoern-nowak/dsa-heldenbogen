import unittest

from parameterized import parameterized

from app.engine import Engine
from app.engine import RulebookProgram
from app.models import Hero
from app.models.rulebook import Rulebook


class TestCommonRules(unittest.TestCase):

    @parameterized.expand([
        (1, ''),
        (0, 'Elf'),
        (1, '_invalid_'),
    ])
    def test_species_known(self, error_count: int, species: str):
        # given:
        engine = Engine([Rulebook.DSA5])
        held = Hero(name="name", species=species, culture='', profession='', talents={})
        # when:
        errors = engine._validate_step(held, RulebookProgram.VALIDATE_HERO_STEP_100)
        # then:
        self.assertIs(error_count, len(errors), msg=errors)

    @parameterized.expand([
        (1, ''),
        (0, 'Auelfen'),
        (1, '_invalid_'),
    ])
    def test_culture_known(self, error_count: int, culture: str):
        # given:
        engine = Engine([Rulebook.DSA5])
        held = Hero(name="name", species='Elf', culture=culture, profession='', talents={})
        # when: actual step is called
        self._check_pre_step(engine, held, RulebookProgram.VALIDATE_HERO_STEP_100)
        errors = engine._validate_step(held, RulebookProgram.VALIDATE_HERO_STEP_200)
        # then:
        self.assertIs(error_count, len(errors), msg=errors)

    @parameterized.expand([
        (0, 'Elf', 'Auelfen'),
        (1, 'Elf', 'Ambosszwerge'),
    ])
    def test_culture_usable(self, error_count: int, species: str, culture: str):
        # given:
        engine = Engine([Rulebook.DSA5])
        held = Hero(name="name", species=species, culture=culture, profession='', talents={})
        # when:
        self._check_pre_step(engine, held, RulebookProgram.VALIDATE_HERO_STEP_100)
        errors = engine._validate_step(held, RulebookProgram.VALIDATE_HERO_STEP_200)
        # then:
        self.assertIs(error_count, len(errors), msg=errors)

    def _check_pre_step(self, engine: Engine, hero: Hero, step: RulebookProgram):
        pre_errors = engine._validate_step(hero, step)
        if pre_errors:
            self.fail(f"Test data (species) incorrect. Hero validation step {step} has errors: {pre_errors}")

    @parameterized.expand([
        (1, ''),
        (0, 'Söldner'),
        (1, '_invalid_'),
    ])
    def test_profession_known(self, error_count: int, profession: str, ):
        # given:
        engine = Engine([Rulebook.DSA5])
        held = Hero(name="name", species='Elf', culture='Auelfen', profession=profession, talents={})
        # when: actual step is called
        self._check_pre_step(engine, held, RulebookProgram.VALIDATE_HERO_STEP_100)
        self._check_pre_step(engine, held, RulebookProgram.VALIDATE_HERO_STEP_200)
        errors = engine._validate_step(held, RulebookProgram.VALIDATE_HERO_STEP_300)
        # then:
        self.assertIs(error_count, len(errors), msg=errors)

    @parameterized.expand([
        (0, 'Elf', 'Auelfen', 'Söldner'),
        (0, 'Elf', 'Auelfen', 'Zauberweber'),
        (1, 'Elf', 'Auelfen', '_invalid_'),
        (1, 'Elf', 'Auelfen', 'Mawdli'),  # requires DSA5_AVENTURISCHES_KOMPENDIUM_2
        (1, 'Zwerg', 'Ambosszwerge', 'Zauberweber'),
    ])
    def test_profession_usable(self, error_count: int, species: str, culture: str, profession: str, ):
        # given:
        engine = Engine([Rulebook.DSA5, Rulebook.DSA5_AVENTURISCHES_KOMPENDIUM_2])
        held = Hero(name="name", species=species, culture=culture, profession=profession, talents={})
        # when: actual step is called
        self._check_pre_step(engine, held, RulebookProgram.VALIDATE_HERO_STEP_100)
        self._check_pre_step(engine, held, RulebookProgram.VALIDATE_HERO_STEP_200)
        errors = engine._validate_step(held, RulebookProgram.VALIDATE_HERO_STEP_300)
        # then:
        self.assertIs(error_count, len(errors), msg=errors)


if __name__ == '__main__':
    unittest.main()
