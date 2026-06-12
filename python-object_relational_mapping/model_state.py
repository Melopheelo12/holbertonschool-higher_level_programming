#!/usr/bin/python3
"""Defines the State class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class definition"""
    __tablename__ = 'states'

    id = Column(
        Integer,
        autoincrement=True,
        primary_key=True
        )

    name = Column(
        String(128),
        nullable=False
        )
