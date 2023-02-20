'''
Please write a program to output a random even number between 0 and 10 inclusive using a random module
and list comprehension.
Use random.choice() to a random element from a list.
'''
import random

my_list = []
for i in range(0,10,2):
    my_list.append(i)

result = random.choice(my_list)

print(result)