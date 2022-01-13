'''
The following functions have problems that keep them from
completing the task that they have to do.

All the problems are either Logical or Syntactical errors with COMMENTS.
Focus on the variables and find the problems with the COMMENTS.

The number of errors are as follows:
volumeCalculator: 2 errors
'''

'''
The goal of this function is to calculate the volume of
an object, when the user inputs height, width, and depth.

The function should print the sentence plus the volume and
return the volume.
'''
def volumeCalculator(height, width, depth):
    area = height * width
    volume = depth * area
    sentence = "The volume of this object is: "
    #This prints out the sentence with the calculated volume.
    print(sentence + volume)
    return volume

#Leave the next line alone
volumeCalculator(5, 5, 5)