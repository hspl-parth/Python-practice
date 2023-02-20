'''
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise
print "No".
Use if statement to judge condition.
'''

string1 = input('Enter the value of string = ')

if string1 == 'Yes':
    print('Yes')
elif string1 == 'yes':
    print('Yes')
elif string1 == 'YES':
    print('Yes')
else:
    print('No')
