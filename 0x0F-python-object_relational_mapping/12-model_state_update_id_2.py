#!/usr/bin/python3
"""
   a script that changes the name of a State object
   with id = 2from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    uri = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(
        uri.format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        state = session.query(State).filter_by(id=2).first()
        state.name = 'New Mexico'
        session.commit()
        print("{}".format(state.name))
    except Exception as err:
        print(err)
    session.close()
