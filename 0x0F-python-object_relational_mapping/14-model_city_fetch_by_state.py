#!/usr/bin/python3
"""This script prints all City objects from the database hbtn_0e_14_usa
"""
from model_city import City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    query_result = session.query(City, State).join(City).order_by(City.id)

    for city_row, state_row in query_result:
        print('{}: ({}) {}'.format(state_row.name, city_row.id, city_row.name))
