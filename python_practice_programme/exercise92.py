'''
By using list comprehension, please write a program to print the list after removing delete numbers which are
divisible by 5 and 7 in [12,24,35,70,88,120,155].
Use list comprehension to delete a bunch of elements from a list.
'''

mylist = [12,24,35,70,88,120,155]

result = [i for i in mylist if (i % 5 != 0 or i % 7 != 0)]

print(result)