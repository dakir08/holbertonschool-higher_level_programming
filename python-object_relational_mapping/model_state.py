#!/usr/bin/python3
"""
contains the class definition of a State
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
DeclarativeBase = declarative_base(metadata=mymetadata)


class State(DeclarativeBase):
    """
    State class
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
