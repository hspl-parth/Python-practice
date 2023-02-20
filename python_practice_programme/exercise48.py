'''
Write a program which can map() and filter() to make a list whose elements are square or even numbers in
[1,2,3,4,5,6,7,8,9,10].
Use map() to generate a list.
Use filter() to filter elements of a list.
Use lambda to define anonymous functions.
'''

list1 = [1,2,3,4,5,6,7,8,9,10]

squarefunction = map(lambda x : x**2, list1)

squareevenfunction = filter(lambda x : x % 2 ==0, squarefunction)

evenfunction = filter(lambda x : x % 2 ==0, list1)

print(list(squareevenfunction))
print(list(evenfunction))