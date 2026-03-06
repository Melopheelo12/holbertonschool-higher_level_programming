#!/usr/bin/python3
"""Adds the State object 'Louisiana' to the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # create engine
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # create new State object
    new_state = State(name="Louisiana")

    # add and commit to database
    session.add(new_state)
    session.commit()

    # print generated id
    print(new_state.id)

    # close session
    session.close()
