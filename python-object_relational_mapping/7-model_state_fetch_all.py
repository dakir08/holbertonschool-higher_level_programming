#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(f"""
                           mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}""")
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id):
        print(state.id, state.name, sep=": ")