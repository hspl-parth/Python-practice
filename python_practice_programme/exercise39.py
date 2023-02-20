'''
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both
included). Then the function needs to print the first 5 elements in the list.
Use ** operator to get the power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list
'''


def function1():
    list1 = []
    for i in range(1, 21):
        value1 = i ** 2
        list1.append(value1)

    print(list1[0:5])

function1()