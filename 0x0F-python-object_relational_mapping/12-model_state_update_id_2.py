#!/usr/bin/python3
"""This script adds the State object “Louisiana” to
the database hbtn_0e_6_usa
"""
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    query_result = session.query(State).order_by(State.id)

    for inst in query_result:
        if inst.id == 2:
            inst.name = 'New Mexico'
    # OR new_state = session.query(state).filter(State.id == 2)
    # new_state.name = 'New Mexico'

    session.commit()
