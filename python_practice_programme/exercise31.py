'''
Define a function that can accept two strings as input and print the string with maximum length in the console.
If two strings have the same length, then the function should print all strings line by line.
'''


def function1():
    string1 = input('Enter the first string = ')
    string2 = input('Enter the second string = ')

    length_of_string1 = len(string1)
    length_of_string2 = len(string2)

    if length_of_string1 > length_of_string2:
        print('Long string is = ', string1)
    elif length_of_string1 < length_of_string2:
        print('Long string is = ', string2)
    else:
        print(f'Both string has same length. string1 is {string1} and string2 is {string2}')

function1()