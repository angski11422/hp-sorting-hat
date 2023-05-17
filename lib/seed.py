

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, House, Result, Question




if __name__ == '__main__':
    engine = create_engine('sqlite:///sortinghat.db')
    Session = sessionmaker(bind=engine)
    session = Session()


    ravenclaw = House(housename="Ravenclaw")
    slytherin = House(housename="Slytherin")
    hufflepuff = House(housename="Hufflepuff")
    gryffindor = House(housename="Gryffindor")

    session.add_all([ravenclaw, slytherin, hufflepuff, gryffindor])
    session.commit()

    q1 = Question(question="Where is your dream vacation?", answer_a="Beach", answer_b="Mountains", value_a="2", value_b="1", value_c="3")
    q2 = Question(question="What is your favorite season?", answer_a="Winter", answer_b="Summer", value_a="1", value_b="2", value_c="4")
    q3 = Question(question="If you could have a super power, what would you choose?", answer_a="Flying", answer_b="Invisibility", value_a="4", value_b="2", value_c="3")
    q4 = Question(question="What would be better?", answer_a="Eat anything, never gain weight", answer_b="Live off 2 hours of sleep", value_a="3", value_b="1", value_c="4")
    q5 = Question(question="You need to tell some one something important:", answer_a="Text", answer_b="Call", value_a="3", value_b="4", value_c="2")
    q6 = Question(question="Your friend is feeling sick, do you?", answer_a="Take them soup and a movie", answer_b="Stay away until they feel better", value_a="4", value_b="2", value_c="1")
    q7 = Question(question="Is the glass?", answer_a="Half Full", answer_b="Half empty", value_a="3", value_b="2", value_c="1")
    q8 = Question(question="How do you destress?", answer_a="Take a bath and read a book", answer_b="Take a walk  or exercise", value_a="3", value_b="1", value_c="4")
    q9 = Question(question="How do your friends describe you?", answer_a="Loyal", answer_b="Adventurous", value_a="3", value_b="4", value_c="2")
    q10 = Question(question="How do you feel about breakfast?", answer_a="Most important meal of the day", answer_b="Skip it", value_a="1", value_b="3", value_c="2")
    q11 = Question(question="If something in your house breaks, you would?", answer_a="Call a professional", answer_b="Fix it yourself", value_a="2", value_b="4", value_c="3")
    q12 = Question(question="At at party, do you?", answer_a="Make new friends/meet new people", answer_b="Stick with your group of friends", value_a="4", value_b="2", value_c="1")
    q13 = Question(question="Who knows you best?", answer_a="Your friends", answer_b="Your family", value_a="4", value_b="3", value_c="1")
    q14 = Question(question="In a zombie apocalypse, would you rather?", answer_a="Go solo, you don't need anyone slowing you down", answer_b="Start survivor camp", value_a="2", value_b="1", value_c="3")
    q15 = Question(question="When someone tells you a secret, the first thing you do is:", answer_a="Take it to the grave", answer_b="Tell everyone you know", value_a="4", value_b="2", value_c="1")
    q16 = Question(question="You are going to sit down and watch some TV:", answer_a="Rewatch an old favorite", answer_b="Find a new show to binge", value_a="3", value_b="1", value_c="4")
    q17 = Question(question="Someone is bullying a stranger nearby:", answer_a="Stand up to them ", answer_b="Ignore them and walk the other way ", value_a="4", value_b="2", value_c="3")
    q18 = Question(question="On a plane, what seat do you choose?", answer_a="Aisle", answer_b="Window", value_a="3", value_b="4", value_c="1")
    q19 = Question(question="What is your favorite time of day?", answer_a="Early bird", answer_b="Night owl", value_a="1", value_b="4", value_c="2")
    q20 = Question(question="Which animal would you rather have as a pet?", answer_a="Dragon", answer_b="Unicorn", value_a="2", value_b="3", value_c="1")

    session.add_all([q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20])
    session.commit()
    session.close()