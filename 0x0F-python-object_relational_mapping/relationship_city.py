#!/usr/bin/python3
"""This Python file similar to model_state.py named model_city.py
that contains the class definition of a City.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import State, Base


class City(Base):
    '''This class links to the MySQL table cities'''

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
