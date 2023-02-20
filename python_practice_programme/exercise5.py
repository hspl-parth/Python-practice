
# Five exercise

'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include a simple test function to test the class methods.
Use __init__ method to construct some parameters
'''

class Myfunction():
    def __init__(self, name):
        self.name = name
        # self.mystring = mystring

    def getString(self):
        mystring = input('Enter your string =')
        print(mystring.upper())
        # print(self.name)

result = Myfunction('Parth')
result.getString()