'''
The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.
Example:
If the following n is given as input to the program:
7
Then, the output of the program should be:
13
In case of input data being supplied to the question, it should be assumed to be a console input.
We can define a recursive function in Python.
'''

num1 = int(input('Enter any number ='))

def fibonacci(num):
    if num == 1 or num == 0:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


print(fibonacci(num1))