#!/usr/bin/python3
"""Defines the City class using SQLAlchemy ORM."""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Represents a city in the database.

    Attributes:
        id (int): Unique identifier of the city.
        name (str): Name of the city.
        state_id (int): Foreign key referencing states.id.
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
