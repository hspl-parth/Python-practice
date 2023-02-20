'''
Write a program which accepts a sequence of words separated by whitespace as input to print the words
composed of digits only.
Example:
If the following words are given as input to the program:
2 cats and 3 dogs.
Then, the output of the program should be:
['2', '3']
In case of input data being supplied to the question, it should be assumed to be a console input.
Use re.findall() to find all substring using regex.
'''

import re

input1 = '2 cats and 3 dogs'

x = re.findall("[0-9]", input1)

print(x)