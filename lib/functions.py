from collections import Counter
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from  models import Question, House, User, Result


engine = create_engine('sqlite:///sortinghat.db')
Session = sessionmaker(bind=engine)
session = Session()

#generate list of random questions
def generate_questions():
    random_questions = session.query(Question).order_by(func.random()).limit(6).all()
    return random_questions
    
#generate results based on user answers
def generate_results(array):
    counter = Counter(array)
    most_common = counter.most_common(1)
    return most_common[0][0] if most_common else None

#query for house info for results
def generate_house():
    house_info = session.query(House).all()
    return house_info

#commit to user table
def commit_name(username):
    user = User(username="username")
    session.add(user)
    session.commit()

#commit to results table
def commit_result(user, house):
    result = Result(user_id=f"{user}", house_id=f"{house}")
    session.add(result)
    session.commit()






    