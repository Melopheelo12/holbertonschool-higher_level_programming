#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a'"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # create database engine
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query states containing 'a'
    states = session.query(State).filter(
        State.name.like("%a%")
    ).order_by(State.id).all()

    # display results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
