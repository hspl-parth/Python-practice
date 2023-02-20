'''
Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
Example:
If the following n is given as input to the program:
5
Then, the output of the program should be:
3.55
In case of input data being supplied to the question, it should be assumed to be a console input.
Use float() to convert an integer to a float
'''

num1 = int(input('Enter the given number = '))
numb2 = 0

for i in range(1, num1+1):
    numb2 = numb2 + float(i)/float(i+1)

print('%.2f'% numb2)