'''
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a
method which can compute the area.
Use def methodName(self) to define a method.
'''


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def methodName(self):
        area = self.length * self.width
        print('Area of the given Rectangle', area)


result = Rectangle(4, 15)
result.methodName()
