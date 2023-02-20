'''
Write a program that accepts a sequence of whitespace separated words as input and prints the words after
removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''

string_input = input('Enter the string which is comma-separated = ')

result = string_input.split()

for i in range(len(result)):
    result[i] = result[i].lower()

no_double = []
for i in range(len(result)):
    if result[i] not in no_double:
        no_double.append(result[i])

no_double.sort()

final = ' '.join(no_double)
print(final)