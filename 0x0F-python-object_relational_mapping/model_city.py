#!/usr/bin/python3
"""
contains the class definition of a City and an
instance Base = declarative_base():
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """ models a table class of Mysql db hbtn_0e_14_usa
        __table_name__(str): the name of the table to be created
        id(sqlalchemy.Integer): the id column
        name(sqlalchemy.String): rep. the name column
        state_id(sqlalchemy.String): rep. the state_id column
    """
    __tablename__ = 'cities'
    id = Column(
        Integer, nullable=False,
        autoincrement=True, primary_key=True,
        unique=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    cities = relationship("State", backref="cities", cascade="all, delete")
