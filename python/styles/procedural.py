from .Person import Person

def calculate_salary(people):
    total = 0
    for p in people:
        total += p.Salary
    return total

def generate_people(n):
    people = []
    for i in range(0, n):
        person = Person.get_random_person(i) 
        people.append(person)
    return people

def run_example():
    print ("== Procedural ==")
    people = generate_people(3)
    for p in people:
        print (p)
    print (calculate_salary(people))
