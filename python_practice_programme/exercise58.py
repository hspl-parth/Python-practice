'''
Write a function to compute 5/0 and use try/except to catch the exceptions.
Use try/except to catch exceptions.
'''


def myfunction():
    try:
        result = 5/0
        print(result)
    except:
        print('This is an exception')


myfunction()