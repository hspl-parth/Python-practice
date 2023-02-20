'''
Write a program to compute:
f(n)=f(n-1)+100 when n>0
and f(0)=1
with a given n input by console (n>0).
Example:
If the following n is given as input to the program:
5
Then, the output of the program should be:
500
In case of input data being supplied to the question, it should be assumed to be a console input.
We can define a recursive function in Python.
'''


num1 = int(input('Enter the given number = '))

def myfunction(x):
    num2 = 0
    if x > 0:
        num2 = myfunction(x - 1) + 100
    return num2

print(myfunction(num1))