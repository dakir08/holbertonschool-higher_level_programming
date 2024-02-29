#!/usr/bin/python3
"""
print city
"""
import sys
from model_state import State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for result in session.query(State.name,
                                City.id, City.name).filter(State.id == City.state_id):
        print(f"{result[0]}: ({result[1]}) {result[2]}")
