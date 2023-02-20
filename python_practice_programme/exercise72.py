'''
Please write a program using a generator to print the even numbers between 0 and n in comma separated
form while n is input by the console.
Example:
If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

num1 = int(input('Enter any number = '))
my_list = []

for i in range(0, num1, 2):
    my_list.append(str(i))

result = ','.join(my_list)
print(result)