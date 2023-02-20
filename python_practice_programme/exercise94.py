'''
By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
Use list comprehension to make an array.
'''

# mylist = []

# for i in range(3):
#     for j in range(5):
#         for k in range(8):
#             mylist.append(0)

mylist = [[[0 for i in range(8)] for j in range(5)] for k in range(3)]

print(mylist)
