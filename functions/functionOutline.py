'''
This outline will help solidify concepts from the Functions lesson.
Fill in this outline as the instructor goes through the lesson.
'''

#1) Make a function that has two boolean parameters. If both booleans are
#true, return true. Else, return false. Then, call the function.
#Print what the function returns.
def addTwoNum(numOne, numTwo):
    answer = numOne + numTwo
    return answer

a = 4
b = 7
addTwoNum(a,b)
sum = addTwoNum(a,b)
print(addTwoNum(a,b))
#2) Make a function that takes one int parameter: gallons. Convert gallons
#to cups (do this by multiplying gallons by 16). Then return cups. Then,
#call the function.
#Print what the function returns.
def convert(gallons):
    cups = gallons * 16
    return cups

g = 3
convert(g)
c = convert(g)
print(convert(g))
#3) Make a function of any any kind with a common SYNTAX error. Then, call the
#function.
#Print what the function returns.
def difference(numOne, numTwo):
answer = numOne - numTwo
return answer

