#!/usr/bin/python3
"""
contains the class definition of a State and an
instance Base = declarative_base():
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ models a state class of Mysql db
        __table_name__(str): the name of the table to be created
        id: the id column
        name: rep. the name column
    """
    __tablename__ = 'states'
    id = Column(
        Integer, nullable=False,
        autoincrement=True, primary_key=True,
        unique=True
    )
    name = Column(String(128), nullable=False)
