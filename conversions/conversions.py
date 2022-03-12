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

#Use input() to get the number of miles from the user. And store
#that int in a variable called miles.
miles = input("Number of miles?")
mileint = int(miles)
#Convert miles to yards, using the following:
# 1 mile = 1760 yards.
yardint = mileint * 1760
#Store the value in a variable called yards and print it out with a 
#simple statement.
yards = ("This is equal to ") + str(yardint) + (" yards.")
print(yards)
#Convert miles to feet, using the following:
# 1 mile = 5280 feet.
feetint = mileint * 5280
#Store the value in a variable called feet and print it out with a 
#simple statement.
feet = ("This is equal to ") + str(feetint) + (" feet.")
print(feet)
#Convert miles to inches, using the following:
# 1 mile = 63,360 inches.
inchint = mileint * 63,360
#Store the value in a variable called inches and print it out with a 
#simple statement.
inches = ("This is equal to ") + str(inchint) + (" inches.")
print(inches)