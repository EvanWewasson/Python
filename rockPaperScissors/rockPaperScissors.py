'''
Created on May 3, 2022
The Objective of this program is to create a game of Rock, Paper, Scissors that
the user can play against the computer.

There should be a loop to repeat the game. And the game should go as follows:
Welcome the user with "Welcome to Rock Paper Scissors! Best two out of three. Press 'q' to quit"
Create variables to keep track of score
Begin a loop to repeat rounds until somebody wins. Someone wins when they have won 2 rounds. (Rounds are outlined below).
Once someone has won, print "Thanks for playing!", print out the final scores, and if the user wins: print "You win!"; if the cpu wins: print "CPU wins!"
Repeat the whole game once someone wins. And until the user chooses to quit.
A round should go as follows:
Have the user choose rock, paper, scissors, or q
Generate a random choice from the computer
Check the users input against the computers choice to see who won the round:
if the user won, add one to the users score, then print out the scores: "User: [#], Computer [#]”
else if the computer won, add one to the computer’s score, then print out the scores: "User: [#], Computer [#]"
else if it was a draw, print "DRAW", then print out the scores: "User: [#], Computer [#]"
else if the user entered "q", then end the round, and the game loop.
else the user didn't enter an accepted input, and prompt them to try again: "Not an option try again."
repeat the round until someone wins.


@author: Evan Wewasson
'''
#import random
import random
from pickle import FALSE
#make a boolean variable called keepPlaying to track whether they want to keep 
#playing and set it to true
keepPlaying = True 
#make a game loop that continues while keepPlaying is true
    #print out a statement that welcomes the user into the game
while(keepPlaying):
    #make variables called userScore and cpuScore to track scores, set to 0
    print("Welcome to Rock Paper Scissors!")
    print("Best two out of three. Press 'q' to quit")
    
    userScore = 0
    cpuScore = 0
    #make a round loop that continues while the userScore or the cpuScore is 
    #less than 2
        #use input to get a choice from the user, (rock, paper, scissors, or q)
        #store the choice in a variable
    while(userScore < 2 and cpuScore < 2):
        choice = input("Please choose (Rock, Paper, Scissor): ")
        #make a list of choices, the use random.choice to get a random choice for the cpu
        #store the choice in a variable
        choiceList = ["rock", "paper", "scissors"]
        cpuChoice = random.choice(choiceList)
        #make a if/elif/else statement to check the user's input against the cpu's 
        #choice. 
        #NOTE: you will have to compare the user's choice and the cpu choice to 
        #(rock, paper, and scissors) seperate and combine with logical operators

        #if the user won, add one to the users score, then print out the scores
        #User : [#], Cpu: [#]
        #-else if the computer won, add one to the users score, then print out
        #the scores: User : [#], Cpu: [#]
        #-else if it was a darw, print "DRAW", then print out the scores: 
        #User : [#], Cpu: [#] 
        #-else if the user entered 'q', then end the round, and the game loop.
        #-else the user didn't enter an accepted input, and prompt them to try
        #again, "Not an option try again"
        if (choice.lower() == 'q'):
            keepPlaying = False 
            break
        elif((choice.lower() == cpuChoice)
             or (choice.lower() == cpuChoice)
             or (choice.lower() == cpuChoice)):
            print("DRAW")
            print("User: " + str(userScore) + " CPU: " + str(cpuScore))
        elif((choice.lower() == "rock" and cpuChoice == "scissors")
             or (choice.lower() == "scissors" and cpuChoice == "paper")
             or (choice.lower() == "paper" and cpuChoice == "rock")):
            userScore = userScore + 1
            print("User: " + str(userScore) + " CPU: " + str(cpuScore))
        elif((choice.lower() == "rock" and cpuChoice == "paper")
             or (choice.lower() == "scissors" and cpuChoice == "rock")
             or (choice.lower() == "paper" and cpuChoice == "scissors")):
            cpuScore = cpuScore + 1 
            print("User: " + str(userScore) + " CPU: " + str(cpuScore))
        else:
            print("Not an option try again.")
            
        #print out thank you message
        print("Thank you for playing!")
        #print out who won:
        #-if the userScore is 2, then the user won
        #-if the cpuSCore is 2, then the cpu won
        if(userScore == 2):
            print("You WIN!")
        elif(cpuScore == 2):
            print("You LOSE!")
        #print out the final scores
        print("User: " + str(userScore) + " CPU: " + str(cpuScore))
        
        

    
    
