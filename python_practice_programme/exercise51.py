'''
Define a class named American which has a static method called printNationality.
Use @staticmethod decorator to define class static method.
'''


class American:
    def __init__(self):
        self.name = 'Parth'

    @staticmethod
    def printNationality():
        nationality = 'American'
        print('in america most of people having nationality of', nationality)

American.printNationality()

