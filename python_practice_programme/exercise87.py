'''
Please write a program to print the running time of execution of "1+1" for 100 times.
Use timeit() function to measure the running time.
'''

import timeit

mycode = '''
def myfunction():
    for i in range(100):
        print('1+1')
'''

print(timeit.timeit(stmt=mycode, number=1))



