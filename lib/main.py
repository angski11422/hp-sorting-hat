#!/usr/bin/env python3
import sys
from functions import *
from time import sleep
from art import *
from models import User, Result
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sortinghat.db')
Session = sessionmaker(bind=engine)
session = Session()

# Add music and art
print(castle)
sleep(.5)
print (welcome)
sleep(1)
in_game = False
while True:
    username_input = input ("What is your name?  ")
    if username_input == "":
        print("Error: Please enter a valid name.")
    else:
        in_game = True
    

    if in_game is True:
        print (f"\nHello {username_input}!")
    ## instructions go here
        sleep(1)
        print ("\nTake a seat and let me explain how the sorting hat works.")
        sleep(1)
        print ("\nI will ask you a series of questions to get an idea of your character.")
        sleep(.5)
        print ("\nYou will answer either a, b, or c")
        sleep(1)
        print ("\nOnce you have reached the end of the questions,")
        sleep(.5)
        print ("\nI will reveal what house you belong to.")
        sleep(1.5)

        take_quiz = input ("\nAre you ready to begin? (yes/no) ").lower()
        if take_quiz == "yes":
            # user = User(username=f"{username_input}")
            # session.add(user)
            # session.commit()

            print ("\nGreat!! Here is your first question\n")
            
            answers = []
            random_questions = generate_questions()
            index = 0

            
            while index < len(random_questions):
                question = random_questions[index]
                print (f"\n{question}")
                q_input = input("Your answer: \n").lower()
                if q_input == "a":
                    answers.append(question.value_a)
                    index += 1
                elif q_input == "b":
                    answers.append(question.value_b)
                    index += 1
                elif q_input == "c":
                    answers.append(question.value_c)
                    index += 1
                else:
                    print ("\nAnswer a, b, or c")
                
            
            most_repeated = generate_results(answers)
            house_info = generate_house()
            print (("\nLet me think..."))
            sleep(5)
            for house in house_info:
                if most_repeated == house.id:
                    print(f"CONGRATS! You are a {house.housename}")
                    for logo in logos:
                        if house.housename == logo.name:
                            print(logo.art)
                    # result = Result(user_id=f"{user.id}", house_id=f"{house.id}")
                    # session.add(result)
                    # session.commit()
                    sys.exit(-1)

                    
        elif take_quiz == "no":
            print ("\nPlease turn in your wand and leave Hogwarts immediately. Goodbye!")
            sys.exit(-1)
            
        else:
            print (f"\nPlease enter yes or no.")
                
                   
                    