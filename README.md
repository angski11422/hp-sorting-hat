# Phase 3 CLI Project 

***
    __  __                                __          
   / / / /___  ____ __      ______ ______/ /______    
  / /_/ / __ \/ __ `/ | /| / / __ `/ ___/ __/ ___/    
 / __  / /_/ / /_/ /| |/ |/ / /_/ / /  / /_(__  )     
/_/ /_/\____/\__, / |__/|__/\__,_/_/   \__/____/      
            /____/                                    
   _____            __  _                
  / ___/____  _____/ /_(_)___  ____ _    
  \__ \/ __ \/ ___/ __/ / __ \/ __ `/    
 ___/ / /_/ / /  / /_/ / / / / /_/ /     
/____/\____/_/   \__/_/_/ /_/\__, /      
                            /____/       
    __  __      __ 
   / / / /___ _/ /_
  / /_/ / __ `/ __/
 / __  / /_/ / /_  
/_/ /_/\__,_/\__/  



### Overview

This is a personality quiz that will ask you a series of questions and then ulimately "sort" you into one of the Hogwarts House's. Based on the Sorting hat ceremony from the Harry Potter series.
All questions and results are ficitious. 

This is done completely in CLI, using some packages for embelishment, such as colorama and playsound.
ASCII art was all found from various resources, not created by me.
Sound clips from various resources, from the Harry Potter movie series.

To run this program in your terminal, install the required packages in the Pipfile.
Run the main.py script in your terminal and follow the prompts.

### Introduction

Brief introduction to the sorting hat with explaination on how it works. Answer a series of questions and get your house results at the end.

### Quiz

Questions will give 4 options, a, b, c, or d. Choose the one that best describes you.
6 questions are randomly generated from a table of questions. Each time you take the quiz, you will get a different set of questions.
Each answer has a value between 1 and 4 which correlates with the id of the housename in the House Table (not all a's are 1's..it varies based on each question).
Answers are collected in an array, and once all 6 questions are answered the quiz is complete and you will wait for the results.

### Results

There is a function that will take the array of answers, map through it and find the most recurring number.
Once it has the most recurring number (or the first one if there is a tie), the next funtion will take that number, search through the House table and find the house id that matches that number. That will return the name of the house.
The program will then display the house results along with some celebratory sounds and images.

### Conclusion

Main.py runs the program
All functions are in the functions.py and passed into the main.py
All art and music is in the art.py file and passed into the main.py
Models.py and Seed.py hold the table models and data respectively



***


