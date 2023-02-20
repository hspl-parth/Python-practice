'''
A website requires the users to input username and password to register. Write a program to check the validity
of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the
above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''

import re

digit_input = input('Enter the your passwords = ')
digit = digit_input.split(',')
my_pass = []

for i in range(len(digit)):
    upper_digit = re.findall('[A-Z]', digit[i])
    lower_digit = re.findall('[a-z]', digit[i])
    number_digit = re.findall('[0-9]', digit[i])
    symbol_digit = re.findall('[@#&]', digit[i])
    # print(len(upper_digit), len(lower_digit), len(number_digit), len(symbol_digit))
    if len(upper_digit) >= 1 and len(lower_digit) >= 1 and len(number_digit) >= 1 and len(symbol_digit) >= 1 and len(digit[i]) > 5 and len(digit[i]) < 12:
        my_pass.append(digit[i])

password = ','.join(my_pass)
print(password)
