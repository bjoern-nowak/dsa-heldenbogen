from typing import List

from pydantic import NonNegativeInt

from app.models import BaseModel
from app.models.hero import Hero as ModelHero


class Hero(BaseModel):
    """
    This is quite a copy of the actual hero model.
    Reasons this still exists:
     - layer separation since this model is used on the api
     - containing api documentation
    """

    name: str

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
            species=self.species,
            culture=self.culture,
            profession=self.profession,
            talents=self.talents,
            combat_techniques=self.combat_techniques,
            advantages=self.advantages,
            disadvantages=self.disadvantages,
        )

    class Config:
        schema_extra = {
            "example": {
                "name": "UncleBob",
                "species": "Elfen",
                "culture": "Auelfen",
                "profession": "Söldner",
                "talents": {"Körperbeherrschung": 3, "Kraftakt": 3, "Selbstbeherrschung": 4, "Zechen": 5, "Menschenkenntnis": 3,
                            "Überreden": 3, "Orientierung": 4, "Wildnisleben": 3, "Götter & Kulte": 3, "Kriegskunst": 6,
                            "Sagen & Legenden": 5, "Handel": 3, "Heilkunde Wunden": 4},
                "combat_techniques": {"Armbrüste": 10, "Raufen": 10, "Stangenwaffen": 9, "Zweihandschwerter": 10},
                "advantages": [("Begabung", "Singen", 1), ("Begabung", "Musizieren", 1), ("Beidhändig", "", 1),
                               ("Dunkelsicht", "", 2)],
                "disadvantages": [("Körpergebundene Kraft", "", 1), ("Lästige Mindergeister", "", 1), ("Wahrer Name", "", 1)]
            }
        }
