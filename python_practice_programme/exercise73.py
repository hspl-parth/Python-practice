'''
Please write a program using a generator to print the numbers which can be divisible by 5 and 7 between 0
and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70
Use yield to produce the next value in the generator.
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

num1 = int(input('Enter any number = '))
my_list = []

for i in range(0, num1):
    if i % 5 == 0 and i % 7 == 0:
        my_list.append(str(i))

result = ','.join(my_list)
print(result)