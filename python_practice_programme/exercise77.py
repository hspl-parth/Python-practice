'''
Please write a binary search function which searches an item in a sorted list. The function should return the
index of the element to be searched in the list.
Use if/elif to deal with conditions.
'''

list1 = ['apple', 'banana', 'cap', 'football', 'cricket']

item1 = input('Enter the item you want to find inside the list = ')

for i in range(len(list1)):
    if item1 == list1[i]:
        print(f'Index number of given {list1[i]} is {i}')
    elif item1 not in list1:
        print('Sorry, this item is not available in list')
        break
