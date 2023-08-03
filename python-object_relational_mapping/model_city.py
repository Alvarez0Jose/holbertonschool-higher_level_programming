#!/usr/bin/python3
'''
File similar to model_state.py that contains the class
definition of a city
'''


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State

Base = declarative_base()


class City(Base):
    '''
    Inherits from Base and links to MySQL 'state'
    '''

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(string(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
