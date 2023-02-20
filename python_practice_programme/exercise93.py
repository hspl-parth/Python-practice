'''
By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th
numbers in [12,24,35,70,88,120,155].
Use list comprehension to delete a bunch of elements from a list.
Use enumerate() to get (index, value) tuple.
'''


mylist = [12,24,35,70,88,120,155]

del mylist[6], mylist[4], mylist[2], mylist[0]

print(mylist)
print(list(enumerate(mylist)))