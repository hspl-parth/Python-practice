'''
Define a function that can receive two integral numbers in string form and compute their sum and then print it
in the console.
'''

num1 = input('Enter the first number = ')
num2 = input('Enter the second number = ')


def sumofthenumber():
    sum = int(num1) + int(num2)
    print('The sum of given numbers is ', sum)


sumofthenumber()