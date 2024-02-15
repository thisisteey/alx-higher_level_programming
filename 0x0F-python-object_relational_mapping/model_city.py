#!/usr/bin/python3
"""A module containing the City model is defined"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """A row in the cities table is represented in this class"""
    __tablename__ = "cities"
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
    state_id = Column(
            Integer,
            ForeignKey('states.id'),
            nullable=False
    )
    state = relationship('State', backref='cities')
