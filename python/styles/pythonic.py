from .Person import Person

def calculate_salary(people):
    return sum(p.Salary for p in people)

def generate_people(n):
    return [Person.get_random_person(i) for i in range(n)]

def run_example():
    print ("== Pythonic ==")
    people = generate_people(3)
    print(*people, sep = "\n")
    print (calculate_salary(people))
