'''
Define a class named Shape and its subclass Square. The Square class has an init function which takes a
length as an argument. Both classes have an area function which can print the area of the shape where the
Shape's area is 0 by default.
To override a method in super class, we can define a method with the same name in the super class.
'''

class Shape:
    def __init__(self, length):
        self.length = length

    def area(self):
        return 0

class Square(Shape):
    def area(self):
        a = 0
        print('The area of given shape is ', a)


result = Square(10)
result.area()