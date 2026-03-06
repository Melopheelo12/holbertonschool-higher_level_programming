#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # create connection
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database),
        pool_pre_ping=True
    )

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # get the first state ordered by id
    state = session.query(State).order_by(State.id).first()

    # print result
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))

    session.close()
