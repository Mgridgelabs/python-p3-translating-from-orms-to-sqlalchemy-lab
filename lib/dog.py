#!/usr/bin/env python3
from sqlalchemy import create_engine
from models import Dog, Base
from sqlalchemy.orm import sessionmaker

# database_url='sqlite:///dogs.db'
def create_table(base, database_url):
    engine = create_engine(database_url)  
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()
    
if __name__ == '__main__':
    DATABASE_URL = 'sqlite:///dogs.db'

    # Create the database and tables
    create_table(Base, DATABASE_URL)

    # Create a new session
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    
    new_dog = Dog(name='Buddy', breed='Golden Retriever')
    save(session, new_dog)

    all_dogs = get_all(session)
    print(all_dogs)

    found_dog = find_by_name(session, 'Buddy')
    print(found_dog)

    update_breed(session, found_dog, 'Labrador')
    updated_dog = find_by_name(session, 'Buddy')
    print(updated_dog)