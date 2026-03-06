#!/usr/bin/python3
"""Defines the State class and Base using SQLAlchemy ORM."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create Base instance
Base = declarative_base()


class State(Base):
    """Represents a state in the database.

    Attributes:
        id (int): The state's unique identifier.
        name (str): The state's name.
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
