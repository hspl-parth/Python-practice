
'''
Write a program that accepts a sequence of lines as input and prints the lines after making all characters in
the sentence capitalised.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''

multiline = []
output = []
while True:
    line = input('Enter your data = ')
    if line:
        multiline.append(line)
        output.append(line.upper())
    else:
        break
    # output.append()

result = '\n'.join(output)
print(result)
