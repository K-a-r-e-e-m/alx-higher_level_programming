#!/usr/bin/python3
'''This module contains the class definition of a State
  and an instance Base = declarative_base()'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    '''This class links to the MySQL table states'''
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete', backref="state")
