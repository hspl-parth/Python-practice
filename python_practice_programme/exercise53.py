'''
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can
compute the area.
Use def methodName(self) to define a method.
'''


class circle:
    def __init__(self, radius):
        self.radius = radius

    def methodName(self):
        area = 3.14 * (self.radius**2)
        print('Area of the given radius', area)


result = circle(4)
result.methodName()

# print(result)