'''
Define a class, which has a class parameter and has the same instance parameter.
'''


class Hellomessage():
    def __init__(self, name):
        self.name = name

    def sayhello(self):
        print(f'Hello {self.name}, Nice to meeet you')


r1 = Hellomessage('Parth')
r1.sayhello()