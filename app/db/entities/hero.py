from typing import TYPE_CHECKING

from sqlalchemy import ARRAY
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import String
from sqlalchemy.orm import relationship

from .base_entity import BaseEntity

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Hero(BaseEntity):
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"), index=True)
    owner = relationship("User", back_populates="heros", index=True)

    name = Column(String, nullable=False, index=True)

    species = Column(String, nullable=False)
    culture = Column(String, nullable=False)
    profession = Column(String, nullable=False)
    talents = Column(JSON, nullable=False)  # dict[str, NonNegativeInt]
    combat_techniques = Column(JSON, nullable=False)  # dict[str, NonNegativeInt]
    advantages = Column(ARRAY, nullable=False)  # List[tuple[str, str, NonNegativeInt]]
    disadvantages = Column(ARRAY, nullable=False)  # List[tuple[str, str, NonNegativeInt]]
