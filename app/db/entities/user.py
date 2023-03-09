from typing import TYPE_CHECKING

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from .base_entity import BaseEntity

if TYPE_CHECKING:
    from .hero import Hero  # noqa: F401


class User(BaseEntity):
    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, index=True, nullable=False)

    hashed_password = Column(String, nullable=False)

    heros = relationship("Hero", back_populates="owner")
