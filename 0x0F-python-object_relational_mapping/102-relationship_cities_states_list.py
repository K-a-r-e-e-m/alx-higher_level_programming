#!/usr/bin/python3
"""This script lists all State objects, and corresponding City objects,
 contained in the database hbtn_0e_101_usa
"""
from relationship_state import State, Base
from relationship_city import City
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
        for city in inst.cities:
            print('{}: {} -> {}'.format(city.id, city.name, inst.name))
