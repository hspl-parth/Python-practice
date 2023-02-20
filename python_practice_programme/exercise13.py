'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
Hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''

seq_input = input('Enter the your sequence = ')
digit = seq_input.split()

count = 0
for i in range(len(digit)):
    for j in digit[i]:
        count += 1

print('Digit in the sequence are = ', len(digit))
print('Letter in the sequence are = ', count)