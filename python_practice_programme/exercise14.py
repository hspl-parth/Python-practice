'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case
letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
import re

seq_input = input('Enter the your sequence = ')
# digit = seq_input.split()

upper_digit = re.findall('[A-Z]', seq_input)
lower_digit = re.findall('[a-z]', seq_input)
print('Upper case =', len(upper_digit))
print('Lower case =', len(lower_digit))


