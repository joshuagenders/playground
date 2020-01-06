import random

class Person():
    Name = ''
    Salary = 50400
    def __init__(self, **kwargs):
        if 'Name' in kwargs:
            self.Name = kwargs['Name']
        if 'Salary' in kwargs:
            self.Salary = kwargs['Salary']
    def __str__(self):
        return '%s earns %s' % (self.Name, self.Salary)
    @staticmethod
    def get_random_person(x):
        return Person(Name = 'Generic person %s' % x, Salary = random.randint(0, 100000))
