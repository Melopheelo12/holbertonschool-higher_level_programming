#!/usr/bin/python3
"""Prints the State id matching the name passed as argument"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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

    # search state safely (SQL injection free)
    state = session.query(State).filter(
        State.name == state_name
    ).first()

    # display result
    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()
