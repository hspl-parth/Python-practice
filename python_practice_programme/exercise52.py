'''
Define a class named American and its subclass NewYorker.
Use class Subclass(ParentClass) to define a subclass.
'''


class American():
    def printNationality(self):
        nationality = 'American'
        print('in america most of people having nationality of', nationality)
        print('This is a superclass')


class NewYorker(American):
    def display2(self):
        print('This is a subclass')


result = NewYorker()
result.printNationality()