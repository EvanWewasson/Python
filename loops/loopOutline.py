'''
This outline will help solidify concepts from the Variables lesson.
Fill in this outline as the instructor goes through the lesson.
'''

#1) Make a int variable called x set to 0. Make a while loop that prints 
#out x and increments it by one. Make the loop run while x is less than
#or equal to 20.
x = 0 
while(x <= 20):
    print(x)
    x = x + 1

#2) Make a int variable called x set to 0. Make a while loop that prints 
#out x and increments it by one. Add an if statement that breaks the loop
#if x equals 15. Make the loop run while x is less than 100.
x = 0
while(x < 100):
    print(x)
    if(x == 15):
        break
    x = x + 1
#3) Make a int list with three items inside. Make a for loop that prints 
#out all the items.
var = [1, 2, 3]
for x in var:
    print(x)
    
    


#4) Make a string list with three items inside: "Michael", "Chris", "Nino". 
#Make a for loop that prints out all the items. Add an if statement that 
#breaks the loop if the item equals "Chris".
list = str("Micheal", "Chris", "Nino")
for x in list:
    print(x)
    
    if (x == "Chris"):
        break

#5) Make a while loop with a common SYNTAX error.
if (x == 5):
break

#6) Make a for loop with a common SYNTAX error.
x == 10
if (r == 4):
    break

