'''
Write a program which can map() to make a list whose elements are squares of numbers between 1 and 20
(both included).
Use map() to generate a list.
Use lambda to define anonymous functions.
'''
import math

list1 = []

for i in range(1, 21):
    list1.append(i)

squarefunction = map(lambda x : x**2, list1)

print(list(squarefunction))