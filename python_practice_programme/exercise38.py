'''
Define a function which can generate and print a list where the values are square of numbers between 1 and
20 (both included).
Use ** operator to get the power of a number.
Use range() for loops.
Use list.append() to add values into a list.
'''

def function1():
    list1 = []
    for i in range(1, 21):
        value1 = i ** 2
        list1.append(value1)

    print(list1)

function1()