'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''

number_input = int(input('Enter the your sequence = '))

first = number_input
second = number_input * 11
third = number_input * 111
four = number_input * 1111

final = first + second + third + four

print(final)