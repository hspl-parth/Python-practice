'''
Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
Use random.sample() to generate a list of random values.
'''
import random

mylist = []

for i in range(100, 201):
    mylist.append(i)

result = random.sample(mylist, k=5)

print(result)