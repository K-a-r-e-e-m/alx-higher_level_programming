#!/usr/bin/python3
"""This script lists all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy.ext.declarative import declarative_base
from model_state import State, Base
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    query_result = session.query(State).order_by(State.id).filter(State.name.like('%a%'))

    for instance in query_result:
        print('{}: {}'.format(instance.id, instance.name))
