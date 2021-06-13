import random
from functools import reduce
from collections import deque
from .Person import Person

get_prop = lambda p : lambda item : getattr(item, p)
mapper = lambda fn : lambda items : map(fn, items)
reducer = lambda fn : lambda items : reduce(fn, items)

get_salary = get_prop('Salary')
get_name = get_prop('Name')

person_to_string = lambda person: f'{get_name(person)} earns {get_salary(person)}'
people_to_string = mapper(person_to_string)
print_list = mapper(print)

get_salaries = mapper(get_salary)
sum_of = lambda a, b: a + b
sum_list = reducer(sum_of)
calculate_total_salary = lambda people : sum_list(get_salaries(people))

generate_people = mapper(Person.get_random_person)

def run_example():
    print ("== Functional ==")
    people = list(generate_people(range(3)))
    deque(print_list(people_to_string(people)), maxlen=0)
    print(calculate_total_salary(people))
