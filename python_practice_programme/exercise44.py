'''
Write a program to generate and print another tuple whose values are even numbers in the given tuple
(1,2,3,4,5,6,7,8,9,10).
Use "for" to iterate the tuple
Use tuple() to generate a tuple from a list.
'''

tuple1 = (1,2,3,4,5,6,7,8,9,10)

list1 = list(tuple1)
even_list = []

for i in list1:
    if i % 2 == 0:
        even_list.append(i)

print('Even number tuple is = ', tuple(even_list))