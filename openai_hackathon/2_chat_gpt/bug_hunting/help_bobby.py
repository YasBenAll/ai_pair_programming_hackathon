"""
Help Bobby Fix His Code


Bobby is troubleshooting a challenge. 
He needs to devise a function whose argument is the size of a square array. 
The function must return the array with the diagonals set to 1 and all the other members set to 0. 
His code is in the Code tab. 
Two of the lines contain bugs. Can you help him?
"""


def help_bobby(size):
    arr = [[[0] * size] * size]
    row = 0
    for column in range(size):
        arr[column][row] = 1
        arr[size - column][row] = 1
        row += 1
    return arr
