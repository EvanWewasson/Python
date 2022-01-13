'''
The following functions have problems that keep them from
completing the task that they have to do.

All the problems are either Logical or Syntactical errors with VARIABLES.
Focus on the variables and find the problems with the VARIABLES.

The number of errors are as follows:
volumeCalculator: 4 errors
shippingAndTax: 3 errors
circleArea: 3 errors
'''

'''
The goal of this function is to calculate the volume of
an object, when the user inputs height, width, and depth.

The function should print the sentence plus the volume and
return the volume.
'''
def volumeCalculator(height, width, depth):
    volume = depth * height * width
    sentence = "The volume of this object is: "
    print(sentence + str(volume))
    return volume

#Leave the next line alone
volumeCalculator(5, 5, 5)

'''
The goal of this function is to calculate the 
total of an order after tax and shipping.

The function should print and
return the total
'''
def shippingAndTax(subTotal):
    shipping = 10
    tax = .10
    
    taxTotal = subTotal * tax
    total = subTotal + taxTotal + shipping
    print("The total is: " + str(total))
    return total

#Leave the next line alone
shippingAndTax(15)

'''
The goal of this function is to calculate the 
total of an order after tax and shipping.

The function should print and
return the total
'''
def circleArea(radius):
    pi = 3.14
    squared = radius * radius
    area = pi * squared 
    print("The area is: " + str(area))
    return area

#Leave the next line alone
circleArea(5)