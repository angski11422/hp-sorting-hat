#!/usr/bin/env python3
import sys
from colorama import Fore, Back, Style, init
import playsound
from functions import *
from time import sleep
from art import *
from models import User, Result
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

init(autoreset = True)
engine = create_engine('sqlite:///sortinghat.db')
Session = sessionmaker(bind=engine)
session = Session()

#"The four houses are called Gryffindor, Hufflepuff, Ravenclaw, and Slytherin. 
# Each house has its own noble history and each has produced outstanding witches and wizards. 
# While you are at Hogwarts, your triumphs will earn your house points, while any rulebreaking will lose house points. 
# At the end of the year, the house with the most points is awarded the house cup, a great honor. 
# I hope each of you will be a credit to whichever house becomes yours.

# "Oh, you may not think I'm pretty,
# But don't judge on what you see,
# I'll eat myself if you can find
# A smarter hat than me.
# You can keep your bowlers black,
# Your top hats sleek and tall,
# For I'm the Hogwarts Sorting Hat
# And I can cap them all.
# There's nothing hidden in your head
# The Sorting Hat can't see,
# So try me on and I will tell you
# Where you ought to be.
# You might belong in Gryffindor,
# Where dwell the brave at heart,
# Their daring, nerve, and chivalry Set Gryffindors apart;
# You might belong in Hufflepuff,
# Where they are just and loyal,
# Those patient Hufflepuffis are true And unafraid of toil;
# Or yet in wise old Ravenclaw,
# if you've a ready mind,
# Where those of wit and learning,
# Will always find their kind;
# Or perhaps in Slytherin
# You'll make your real friends,
# Those cunning folk use any means
# To achieve their ends.
# So put me on! Don't be afraid!
# And don't get in a flap!
# You're in safe hands (though I have none)
# For I'm a Thinking Cap!"

# Add music
print(Back.CYAN+castle)
sleep(.5)
print (Fore.CYAN+welcome)
sleep(1)
in_game = False
while True:
    username_input = input (Fore.MAGENTA+Style.BRIGHT+"What is your name?  ")
    if username_input == "":
        print(Fore.RED+Style.BRIGHT+"Error: Please enter a valid name.")
    else:
        in_game = True
    

    if in_game is True:
        print (f"\nHello {username_input}!")
    ## instructions go here
        sleep(1)
        print (Fore.MAGENTA+"\nTake a seat and let me explain how the sorting hat works.")
        sleep(1)
        print (Fore.MAGENTA+"\nI will ask you a series of questions to get an idea of your character.")
        sleep(.5)
        print (Fore.MAGENTA+"\nYou will answer either a, b, or c")
        sleep(1)
        print (Fore.MAGENTA+"\nOnce you have reached the end of the questions,")
        sleep(.5)
        print (Fore.MAGENTA+"\nI will reveal what house you belong to.")
        sleep(1.5)

        take_quiz = input (Fore.GREEN+"\nAre you ready to begin? (yes/no) ").lower()
        if take_quiz == "yes":
            # user = User(username=f"{username_input}")
            # session.add(user)
            # session.commit()

            print (Fore.GREEN+Style.BRIGHT+"\nGreat!! Here is your first question\n")
            
            answers = []
            random_questions = generate_questions()
            index = 0

            
            while index < len(random_questions):
                question = random_questions[index]
                print (Fore.GREEN+f"\n{question}")
                q_input = input(Style.BRIGHT+"Your answer: \n").lower()
                if q_input == "a":
                    answers.append(question.value_a)
                    print(Style.RESET_ALL)
                    index += 1
                elif q_input == "b":
                    answers.append(question.value_b)
                    print(Style.RESET_ALL)
                    index += 1
                elif q_input == "c":
                    answers.append(question.value_c)
                    print(Style.RESET_ALL)
                    index += 1
                else:
                    print (Fore.RED+Style.BRIGHT+"\nAnswer a, b, or c")
                
            
            most_repeated = generate_results(answers)
            house_info = generate_house()
            print (Fore.CYAN+Style.BRIGHT+("\nLet me think..."))
            print (Fore.CYAN+Style.BRIGHT+wand)
            sleep(5)
            for house in house_info:
                if most_repeated == house.id:
                    for logo in logos:
                        if house.housename == logo.name:
                            color = getattr(Fore, logo.color)
                            print(color+Style.BRIGHT+f"CONGRATS! You are a {house.housename}")
                            print(color+Style.BRIGHT+logo.art)
                    # result = Result(user_id=f"{user.id}", house_id=f"{house.id}")
                    # session.add(result)
                    # session.commit()
                    print (Fore.CYAN+"Now go join your house and have a great year!")
                    sys.exit(-1)

                    
        elif take_quiz == "no":
            print (Fore.RED+Back.WHITE+"\nPlease turn in your wand and leave Hogwarts immediately. Goodbye!")
            sys.exit(-1)
            
        else:
            print (Fore.RED+Style.BRIGHT+f"\nPlease enter yes or no.")
                
                   
                    