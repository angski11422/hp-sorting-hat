import random
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from  models import Question

# error_message = "Please enter a valid answer"
# c = "Neither"


if __name__ == '__main__':
        engine = create_engine('sqlite:///sortinghat.db')
        Session = sessionmaker(bind=engine)
        session = Session()

        random_questions = session.query(Question.question).first()
        print(random_questions)
        
        

   