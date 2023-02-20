'''
Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
Use random.sample() to generate a list of random values.
'''

import random

mylist = []

for i in range(100, 201):
    if i % 2 == 0:
        mylist.append(i)

result = random.sample(mylist, k=5)

print(result)