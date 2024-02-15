#!/usr/bin/python3
"""A module containing the state model is defined"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
"""The base class for all tables is represented using a common structure"""


class State(Base):
    """A state from the states table is represnted in this class"""
    __tablename__ = "states"
    id = Column(
            Integer,
            autoincrement=True,
            unique=True,
            nullable=False,
            primary_key=True
    )
    name = Column(
            String(length=128),
            nullable=False
    )
