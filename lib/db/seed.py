from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, House, Result


fake = Faker()

if __name__ == '__main__':
    engine = create_engine('sqlite:///sortinghat.db')
    Session = sessionmaker(bind=engine)
    session = Session()


    ravenclaw = House(housename="Ravenclaw")
    slytherin = House(housename="Slytherin")
    hufflepuff = House(housename="Hufflepuff")
    gryffindor = House(housename="Gryffindor")

    # session.add_all([ravenclaw, slytherin, hufflepuff, gryffindor])
    # session.commit()

