from .Person import Person

class PeopleFactory():
    def create_people(self, n):
        people = []
        for i in range(n):
            people.append(Person.get_random_person(i))
        return people

class PeopleAnalyzer():
    def __init__(self, peopleFactory):
        self.peopleFactory = peopleFactory
        self.people = []
        self.total_salary = 0
    def analyze(self, count):
        self.people = self.peopleFactory.create_people(count)
        self.total_salary = sum(p.Salary for p in self.people)
    def print_all(self):
        for p in self.people:
            print(p)
    def get_total_salary(self):
        return self.total_salary

def run_example():
    print ("== Object Oriented ==")
    people_analyzer = PeopleAnalyzer(PeopleFactory())
    people_analyzer.analyze(3)
    people_analyzer.print_all()
    print (people_analyzer.get_total_salary())
