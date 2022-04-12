'''
Created on Mar 11, 2022
The Objective of this program is to quiz the user on basic high school
trivia. The tasks to complete are:
Ask the user each of the following questions:
    1) What is the powerhouse of the cell?
        A) mitochondria B) nucleus C) ribosome
    2) How many states comprise the United States?
        A) 13 B) 45 C) 50
    3) In y = mx + b, what does m stand for?
        A) slope B) output C) I don't understand math
    4) In English, a person, place or thing is called:
        A) verb B) adjective C) noun
The user should input a letter for each question. (A, B, or C)
Check the users answer, if it is correct print "Correct", 
else it should print "Incorrect, the correct answer is [insert]"
Additionally, the program should track how many questions the user got correct 
and at the end give them a score out of 4. And give them a percentage.

@author: Evan Wewasson
'''

'''
userResponse = input(text_to_user)
'''

score = 0

print("1) What is the powerhouse of the cell?")
one = input("Enter a letter: A) mitochondria B) nucleus C) ribosome")

if (one.upper() =="A"):
    score= score + 1
    print("Correct")
else:
    print("Incorrect, the correct answer is A.")

print("2) How many states comprise the United States?")
two = input("Enter a letter: A) 13 B) 45 C) 50")

if (two.upper() =="C"):
    score = score + 1
    print("Correct")
else:
    print("Incorrect, the correct answer is C.")

print("3) In y = mx + b, what does m stand for?")
three = input("Enter a letter: A) slope B) output C) I don't understand math")

if (three.upper() =="A"):
    score = score + 1
    print("Correct")
else:
    print("Incorrect, the correct answer is A.")

print("4) In English, a person, place or thing is called:")
four = input("Enter a letter: A) verb B) adjective C) noun")

if (four.upper() =="C"):
    score = score + 1
    print("Correct")
else:
    print("Incorrect, the answer is C.")

p = (score / 4) * 100

print("You got a " + str(score) + "/4. Or a " + str(p) + "%.")