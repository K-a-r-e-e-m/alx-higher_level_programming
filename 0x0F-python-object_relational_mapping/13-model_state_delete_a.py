#!/usr/bin/python3
"""This script deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
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

    new_state = session.query(State).filter(State.name.contains('a')).delete()
    session.commit()
