#!/usr/bin/python3
"""Updates the name of the State object where id = 2"""

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

    # find state with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # update name if state exists
    if state:
        state.name = "New Mexico"
        session.commit()

    # close session
    session.close()
