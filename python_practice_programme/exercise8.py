
# Eight exercise

'''
Write a program that accepts a comma separated sequence of words as input and prints the words in a
comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''

string_input = input('Enter the string which is comma-separated = ')

result = string_input.split(',')

for i in range(len(result)):
    result[i] = result[i].lower()

result.sort()

final = ','.join(result)

print(final)
