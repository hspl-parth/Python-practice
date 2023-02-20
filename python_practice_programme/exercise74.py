'''
Please write assert statements to verify that every number in the list [2,4,6,8] is even.
Use "assert expression" to make an assertion.
'''

list1 = [2,4,6,8,9]

for i in list1:
    assert i%2 == 0, f'{i} is not even number'