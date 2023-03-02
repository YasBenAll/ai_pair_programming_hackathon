"""
Help Bobby Fix His Code


Bobby is troubleshooting a challenge. 
He needs to devise a function whose argument is the size of a square array. 
The function must return the array with the diagonals set to 1 and all the other members set to 0. 
His code is in the Code tab. 
Two of the lines contain bugs. Can you help him?
"""
import numpy as np 

def help_bobby(size):
    arr = [[[0] * size] * size]
    row = 0
    for column in range(size):
        arr[column][row] = 1
        arr[size - column][row] = 1
        row += 1
    return arr

def help_bobby_GPT(size):
    arr = np.zeros((size, size))
    for i in range(size):
        arr[i, i] = 1
        arr[i, size - i - 1] = 1
    return arr

if __name__ == "__main__":
    # print(help_bobby(5))
    print(help_bobby_GPT(5))