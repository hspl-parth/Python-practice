
# Eleven exercise

'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then
check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma
separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
'''
import math

digit_input = input('Enter the 4 digit binary numbers = ')
digit = digit_input.split(',')
my_num = []

for i in range(len(digit)):
    if len(digit[i]) == 4 and digit[i][0] != '0':
        # digit = digit_input.split(',')
        if int(digit[i]) % 5 == 0:
            my_num.append(digit[i])
    # else:
    #     print('Please enter the 4 digit binary numbers')

final = ','.join(my_num)

print(final)