'''
Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].
Use list comprehension to delete a bunch of elements from a list.
'''

mylist = [5,6,77,45,22,12,24]

result = [i for i in mylist if i % 2 != 0]

# for i in mylist:
#     if i % 2 != 0:
#         result.append(i)

print(result)
