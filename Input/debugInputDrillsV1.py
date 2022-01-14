'''
The following functions have problems that keep them from
completing the task that they have to do.

All the problems are either Logical or Syntactical errors with INPUT.
Focus on the variables and find the problems with the INPUT FUNCTION.

The number of errors are as follows:
circleArea: 1
rectangleArea: 2
'''

'''
The goal of this function is to calculate the 
area of a circle.

The function gets a radius from the user and 
then calculates the area.

The function should print and
return the area.
'''
def circleArea():
    radius = input"What is the radius of your circle?")
    
    pi = 3.14
    squared = int(radius) * int(radius)
    area = pi * squared 
    print("The area is: " + area)
    return area

#Leave the next line alone
circleArea()



'''
This function calculates the area of a rectangle.

The function gets a height and width from the user and then calculates
the area.

The function prints and returns the area.
'''
def rectangleArea():
    = input("What is the height of your rectangle?")
    width = input()
    
    area = int(height) * int(width)
    print(area)
    return area

#Leave the next line alone
rectangleArea()