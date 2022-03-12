'''
Created on Mar 11, 2022

The Objective is to make a program that can complete different conversions. 
The tasks to complete are:
Have the user input a number of miles.
Convert the number of miles to yards, feet, and inches.
Print out the conversions with a simple statement.

@author: Evan Wewasson
'''

'''
userResponse = input(text_to_user)
'''


miles = input("Number of miles?")
mileint = int(miles)

yardint = mileint * 1760

yards = ("This is equal to ") + str(yardint) + (" yards.")
print(yards)

feetint = mileint * 5280

feet = ("This is equal to ") + str(feetint) + (" feet.")
print(feet)

inchint = mileint * 63360

inches = ("This is equal to ") + str(inchint) + (" inches.")
print(inches)