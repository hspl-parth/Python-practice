'''
Please write a program which prints all permutations of [1,2,3]
Use itertools.permutations() to get permutations of lists.
'''

import itertools

list1 = [1,2,3]

number1 = itertools.permutations(list1)

print(list(number1))