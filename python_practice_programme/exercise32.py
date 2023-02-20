'''
Define a function that can accept an integer number as input and print "It is an even number" if the number is
even, otherwise print "It is an odd number".
'''

number1 = int(input('Enter any number = '))

if number1 % 2 == 0:
    print('The given number is even')
else:
    print('THe given number is odd')