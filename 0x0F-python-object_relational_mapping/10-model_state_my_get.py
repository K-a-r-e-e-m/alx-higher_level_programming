#!/usr/bin/python3
'''This module prints the State object with the name
   passed as argument from the database '''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    query_result = Session().query(State).order_by(State.id)

    found = False
    for instance in query_result:
        if instance.name == argv[4]:
            found = True
            break
    if (found):
        print(instance.id)
    else:
        print('Not found')
