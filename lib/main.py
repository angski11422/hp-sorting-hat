#!/usr/bin/env python3

error_message = "Please enter a valid answer"
c = "Neither"

print ("Welcome to Hogwarts!!")

username_input = input ("\nWhat is your name?  ")

print (f"\nHello {username_input}!")

## instructions go here
print ("\nTake a seat and let me explain how the sorting hat works.\n")
print ("I will ask you a series of questions to get an idea of your character.\nOnce you have reached the end of the questions, \nI will reveal what house you belong to.")

take_quiz = input ("\nAre you ready to begin? (yes/no) ").lower()
if take_quiz == "yes":
    print ("\nHere is your first question")
    q1_answer = input (f"\nWhere is your dream vacation? \na. Beach \nb. Mountains \nc. {c} \n").lower()
    
    if  q1_answer == "a":
        q2_answer = input (f"\nWhat is your favorite season? \na. Winter \nb. Summer \nc. {c} \n").lower()
        if q2_answer == "a":
            r1_answer = input (f"\nIf you could have a super power, what would you choose? \na. Flying \nb. Invisibility \nc. {c} \n").lower()
            if r1_answer == "a":
                r2_answer = input(f"\nYour friend is feeling sick, do you? \na. Take them soup and a movie \nb. Stay away \nc. {c} \n").lower()
                if r2_answer == "a":
                    r3_answer = input(f"\nHow do you feel about breakfast? \na. Most important meal of the day \nb. Skip it \nc. {c} \n").lower()
                    if r3_answer == "a":
                        r4_answer = input(f"\nIn a zombie apocalypse, would you? \na. Go solo, you don't need anyone slowing you down \nb. Start survivor camp \nc. {c} \n").lower()
                        if r4_answer == "b":
                            print (f"Congrats! You are a Ravenclaw")

    elif q1_answer == "b":
        q2_answer = input (f"\nWhat is your favorite season? \na. Spring \nb. Fall \nc. {c} \n").lower()

    elif q1_answer == "c":
        q2_answer = input (f"\nWhat is your favorite season? \na. Summer \nb. Fall \nc. {c} \n").lower()

    else:
        print (f"{error_message}")
            

else:
    print ("\nPlease turn in your wand and leave Hogwarts immediately")