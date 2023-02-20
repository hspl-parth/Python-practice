'''
Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included)
and the values are square of keys.
'''

dict1 = {}

for i in range(1, 21):
    key1 = i
    value1 = i**2
    # print(key1, value1)
    dict1[key1] = value1

print(dict1)