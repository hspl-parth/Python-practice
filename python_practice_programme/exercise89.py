'''
Please write a program which accepts a string from the console and print the characters that have even
indexes.
Example:
If the following string is given as input to the program:
H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:
Helloworld
Use list[::2] to iterate a list by step 2.
'''

mystr = input('Please enter the string = ')

result = mystr[::2]

print(result)