'''
Define a function that can accept two strings as input and concatenate them and then print it in the console.
'''

string1 = input('Enter the first string = ')
string2 = input('Enter the second string = ')


def ConcatenateString():
    total = string1 + string2
    print('Your new string will be = ', total)

ConcatenateString()