'''
Define a custom exception class which takes a string message as an attribute.
To define a custom exception, we need to define a class inherited from Exception.
'''


class Exception:
    def __init__(self, message):
        self.message = message

    def stringmessage(self):
        print('The message from Original exception class')


class InheritedException(Exception):
    def stringmessage(self):
        print('The message from inherited exception class')

result = InheritedException('Hello')
result.stringmessage()