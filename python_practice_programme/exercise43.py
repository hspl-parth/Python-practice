'''
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last
half values in one line.
Use [n1:n2] notation to get a slice from a tuple.
'''

tuple1 = (1,2,3,4,5,6,7,8,9,10)

list1 = list(tuple1)

first_half = list1[0:5]
second_half = list1[5:]

print('First half of the given tuple', tuple(first_half))
print('Second half of the given tuple', tuple(second_half))