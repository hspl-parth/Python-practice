'''
Please write a program which accepts a string from the console and print it in reverse order.
Example:
If the following string is given as input to the program:
rise to vote sir
Then, the output of the program should be:
ris etov ot esir
Use list[::-1] to iterate a list in a reverse order.
'''

mylist = input('Enter your string = ')

result = mylist[::-1]

print(result)