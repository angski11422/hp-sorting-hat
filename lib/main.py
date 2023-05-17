#!/usr/bin/env python3
from functions import *
from time import sleep

# Add music and art

print ("Welcome to Hogwarts!!")

username_input = input ("\nWhat is your name?  ")

print (f"\nHello {username_input}!")

## instructions go here
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
        elif q_input == "b":
            answers.append(question.value_b)
        elif q_input == "c":
            answers.append(question.value_c)
        else:
            print ("Please choose a valid answer")
        index += 1
 
    print(answers)
    
            
elif take_quiz == "no":
    print ("\nPlease turn in your wand and leave Hogwarts immediately. Goodbye!")
else:
    print (f"\nPlease enter yes or no.")
    
    