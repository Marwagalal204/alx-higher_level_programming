#!/usr/bin/python3

""" class definition of a State and an instance Base"""
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """Class with id, name attributes of each state"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
