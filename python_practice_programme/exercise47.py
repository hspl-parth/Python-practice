'''
Write a program which can map() to make a list whose elements are square of elements in
[1,2,3,4,5,6,7,8,9,10].
Use map() to generate a list.
Use lambda to define anonymous functions.
'''

list1 = [1,2,3,4,5,6,7,8,9,10]

myfunction = map(lambda x : x**2, list1)

print(list(myfunction))
