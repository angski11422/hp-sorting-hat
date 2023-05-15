#!/usr/bin/env python3

print ("Welcome to Hogwarts!!")

username_input = input ("\nWhat is your name?  ")

print (f"\nHello {username_input}!")

## instructions go here
print ("\nTake a seat and let me explain how the sorting hat works.\n")
print ("I will ask you a series of questions to get an idea of your character.\nOnce you have reached the end of the questions, \nI will reveal what house you belong to.")

take_quiz = input ("\nAre you ready to begin?  ").lower()
if take_quiz == "yes":
    print ("\nHere is your first question")
else:
    print ("\nPlease turn in your wand and leave Hogwarts immediately")