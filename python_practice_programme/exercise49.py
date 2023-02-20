'''
Write a program which can filter() to make a list whose elements are an even number between 1 and 20 (both
included).
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.
'''

list1 = []

for i in range(1, 21):
    list1.append(i)

evenfunction = filter(lambda x : x % 2 == 0, list1)

print(list(evenfunction))