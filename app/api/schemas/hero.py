from typing import List

from pydantic import NonNegativeInt

from app.models.base_model import BaseModel
from app.models.dis_advantage import DisAdvantage
from app.models.experience_level import ExperienceLevel
from app.models.hero import Hero as ModelHero
from app.models.skill import Skill


# TODO rename to SchemaHero whenever name can be keep Hero in api
class Hero(BaseModel):
    """
    This is quite a copy of the actual hero model.
    Reasons this still exists:
     - layer separation since this model is used on the api
     - containing api documentation
     - simplified data structure for improved readability
    """

    name: str

    experience_level: ExperienceLevel

    species: str
    culture: str
    profession: str

    talents: dict[str, NonNegativeInt]
    combat_techniques: dict[str, NonNegativeInt]

    # TODO add api documentation: tuples second entry must be set but can be empty
    advantages: List[tuple[str, str, NonNegativeInt]]
    disadvantages: List[tuple[str, str, NonNegativeInt]]

    def to_model(self) -> ModelHero:
        return ModelHero(
            name=self.name,
            experience_level=self.experience_level,
            species=self.species,
            culture=self.culture,
            profession=self.profession,
            talents=Hero._dict_to_skills(self.talents),
            combat_techniques=Hero._dict_to_skills(self.combat_techniques),
            advantages=Hero._tuples_to_dis_advantages(self.advantages),
            disadvantages=Hero._tuples_to_dis_advantages(self.disadvantages),
        )

    @staticmethod
    def _dict_to_skills(dict_: dict[str, NonNegativeInt]) -> List[Skill]:
        return [Skill(name=key, level=dict_[key]) for key in dict_]

    @staticmethod
    def _tuples_to_dis_advantages(tuples: List[tuple[str, str, NonNegativeInt]]) -> List[DisAdvantage]:
        return [DisAdvantage(name=name, uses=uses, level=level) for name, uses, level in tuples]

    class Config:
        schema_extra = {
            "examples": {
                "valid_with_warnings": {
                    "summary": "[VALID] OK but having warnings",
                    "value": {
                        "name": "UncleBob",
                        "experience_level": "Legendary",
                        "species": "Elfen",
                        "culture": "Auelfen",
                        "profession": "Söldner",
                        "talents": {"Körperbeherrschung": 3, "Kraftakt": 3, "Selbstbeherrschung": 4, "Zechen": 5,
                                    "Menschenkenntnis": 3, "Überreden": 3, "Orientierung": 4, "Wildnisleben": 3,
                                    "Götter & Kulte": 3,
                                    "Kriegskunst": 6, "Sagen & Legenden": 5, "Handel": 3, "Heilkunde Wunden": 4},
                        "combat_techniques": {"Armbrüste": 10, "Raufen": 10, "Stangenwaffen": 9, "Zweihandschwerter": 10},
                        "advantages": [("Begabung", "Singen", 1), ("Begabung", "Musizieren", 1), ("Beidhändig", "", 1),
                                       ("Dunkelsicht", "", 2)],
                        "disadvantages": [("Körpergebundene Kraft", "", 1), ("Lästige Mindergeister", "", 1),
                                          ("Wahrer Name", "", 1)]
                    }
                },
                "invalid_unknown_value": {
                    "summary": "[INVALID] Unknown species value",
                    "value": {
                        "name": "UncleBob",
                        "experience_level": "Legendary",
                        "species": "Elfen",
                        "culture": "Auelfen",
                        "profession": "Söldnera",
                        "talents": {"Körperbeherrschung": 3, "Kraftakt": 3, "Selbstbeherrschung": 4, "Zechen": 5,
                                    "Menschenkenntnis": 3, "Überreden": 3, "Orientierung": 4, "Wildnisleben": 3,
                                    "Götter & Kulte": 3,
                                    "Kriegskunst": 6, "Sagen & Legenden": 5, "Handel": 3, "Heilkunde Wunden": 4},
                        "combat_techniques": {"Armbrüste": 10, "Raufen": 10, "Stangenwaffen": 9, "Zweihandschwerter": 10},
                        "advantages": [("Begabung", "Singen", 1), ("Begabung", "Musizieren", 1), ("Beidhändig", "", 1),
                                       ("Dunkelsicht", "", 2)],
                        "disadvantages": [("Körpergebundene Kraft", "", 1), ("Lästige Mindergeister", "", 1),
                                          ("Wahrer Name", "", 1)]
                    }
                },
                "invalid_missing_level": {
                    "summary": "[INVALID] Talent not an required minimum level",
                    "value": {
                        "name": "UncleBob",
                        "experience_level": "Legendary",
                        "species": "Elfen",
                        "culture": "Auelfen",
                        "profession": "Söldner",
                        "talents": {"Körperbeherrschung": 2, "Kraftakt": 3, "Selbstbeherrschung": 4, "Zechen": 5,
                                    "Menschenkenntnis": 3, "Überreden": 3, "Orientierung": 4, "Wildnisleben": 3,
                                    "Götter & Kulte": 3,
                                    "Kriegskunst": 6, "Sagen & Legenden": 5, "Handel": 3, "Heilkunde Wunden": 4},
                        "combat_techniques": {"Armbrüste": 10, "Raufen": 10, "Stangenwaffen": 9, "Zweihandschwerter": 10},
                        "advantages": [("Begabung", "Singen", 1), ("Begabung", "Musizieren", 1), ("Beidhändig", "", 1),
                                       ("Dunkelsicht", "", 2)],
                        "disadvantages": [("Körpergebundene Kraft", "", 1), ("Lästige Mindergeister", "", 1),
                                          ("Wahrer Name", "", 1)]
                    }
                }
            }
        }
