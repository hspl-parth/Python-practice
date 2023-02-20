'''
Use a list comprehension to square each odd number in a list. The list is input by a sequence of
comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9
'''


digit_input = input('Enter the your sequence = ')
digit = digit_input.split(',')
my_num = []

# for i in range(len(digit)):
for j in range(0, len(digit), 2):
    my_num.append(digit[j])

result = ','.join(my_num)
print(result)