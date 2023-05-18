#!/usr/bin/env python3
from functions import *
from time import sleep
import sys
from models import User, Result

# Add music and art

print ("Welcome to Hogwarts!!")
sleep(1)
in_game = False
while True:
    username_input = input ("What is your name?  ")
    if username_input == "":
        print("Error: Please enter a valid name.")
    else:
        in_game = True
    
    # push username to table

    
    if in_game is True:
        print (f"\nHello {username_input}!")
    ## instructions go here
        sleep(1)
        print ("\nTake a seat and let me explain how the sorting hat works.\n")
        sleep(1)
        print ("\nI will ask you a series of questions to get an idea of your character.")
        sleep(1)
        print ("\nOnce you have reached the end of the questions,")
        sleep(.5)
        print ("\nI will reveal what house you belong to.")
        sleep(1.5)

    
        take_quiz = input ("\nAre you ready to begin? (yes/no) ").lower()
        if take_quiz == "yes":
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
            for house in house_info:
                if most_repeated == house.id:
                    print(f"CONGRATS! You are a {house.housename}")
                    sys.exit(-1)
                        

        # post result to table
                    
        elif take_quiz == "no":
            print ("\nPlease turn in your wand and leave Hogwarts immediately. Goodbye!")
            sys.exit(-1)
            
        else:
            print (f"\nPlease enter yes or no.")
                
                   
                    