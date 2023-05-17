import random
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from  models import Question




engine = create_engine('sqlite:///sortinghat.db')
Session = sessionmaker(bind=engine)
session = Session()

def generate_questions():
    random_questions = session.query(Question).order_by(func.random()).limit(6).all()
   
    return random_questions
    
    
        

    