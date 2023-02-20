'''
Please write a program which accepts basic mathematical expression from console and print the evaluation
result.
Example:
If the following string is given as input to the program:
35+3
Then, the output of the program should be:
38
Use eval() to evaluate an expression.
'''

str1 = input('Enter the string here =')
# digit = str1.split('+')
#
# def sum(x, y):
#     total = int(x) + int(y)
#     print(total)

# sum(digit[0], digit[1])

sum = eval(str1)
print(sum)