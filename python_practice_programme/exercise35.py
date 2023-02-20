'''
Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both
included) and the values are square of keys. The function should just print the values only.
'''

dict1 = {}

for i in range(1, 21):
    key1 = i
    value1 = i**2
    dict1[key1] = value1


for keys, values in dict1.items():
    print('Values of the dictionary is = ', values)

