from collections import Counter
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from  models import Question, House




engine = create_engine('sqlite:///sortinghat.db')
Session = sessionmaker(bind=engine)
session = Session()

def generate_questions():
    random_questions = session.query(Question).order_by(func.random()).limit(6).all()
    return random_questions
    
    
def generate_results(array):
    counter = Counter(array)
    most_common = counter.most_common(1)
    return most_common[0][0] if most_common else None

def generate_house():
    house_info = session.query(House).all()
    return house_info






    