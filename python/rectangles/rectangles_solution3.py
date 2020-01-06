from itertools import permutations
from functools import reduce

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.joined_x = None
        self.joined_y = None
    def __str__(self):
        return f"{self.x},{self.y}"
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash(f"{self.x}:{self.y}")

def traverse_array(input_arr, starting, finishing, levels):
    if levels > 1:
        for x in range(starting, finishing - (levels - 1)):
            for nxt in traverse_array(input_arr, x + 1, finishing, levels - 1):
                yield [input_arr[x]] + nxt
    else:
        for current in range(starting + levels - 1, finishing):
            yield [input_arr[current]]

def unique_permutations_of_length(input_arr, length):
    unique_list = list(set(input_arr))
    return traverse_array(unique_list, 0, len(unique_list), length)

def try_join(p1, p2):
    if p1.x == p2.x:
        return (True, 'y') # return opposite axis
    if p1.y == p2.y:
        return (True, 'x')
    return (False, None)

def count_rectangles(points):
    point_permutations = [[p, is_rectangle(p[0], p[1], p[2], p[3])] for p in unique_permutations_of_length(points, 4)]
    return reduce(lambda acc, x: acc + 1 if x[1] else acc, point_permutations, 0)

# Construct rectangle by finding joining points
def is_rectangle(p1,p2,p3,p4):
    r1 = p1
    r2 = None
    r3 = None
    r4 = None
    points = [p2,p3,p4]
    # try join a point on x or y axis
    for p in points:
        r = try_join(r1, p)
        if (r[0]):
            r2 = p
            next_axis = r[1]
            break
    if r2:
        points.remove(r2)
    else:
        return False # no joining point found

    #find another joining point
    for p in points:
        if getattr(p, next_axis) == getattr(r2, next_axis):
            r3 = p
            next_axis = get_opposite(next_axis)
            break
    if r3:
        points.remove(r3)
    else:
        return False # no joining point found

    # if the final point joins
    r4 = points[0]
    opposite_axis = get_opposite(next_axis)
    if getattr(r4, next_axis) == getattr(r3, next_axis) and getattr(r4, opposite_axis) == getattr(r1, opposite_axis):
        return True
    return False # Final point doesn't join

def get_opposite(axis):
    return 'x' if axis == 'y' else 'y'

def print_example(data, prompt):
    print(prompt)
    print(f"Number of rectangles is {count_rectangles(data)}")

if __name__ == "__main__":
    prompt = '''
    Y
    3
    2 o o
    1 o o o
    0 o o o
    X 0 1 2 3
    '''
    data = [
        Point(0,0), Point(0,1), Point(0,2),
        Point(1,0), Point(1,1), Point(1,2),
        Point(2,0), Point(2,1)
    ]
    print_example(data, prompt)

    prompt = '''
    Y
    3
    2 
    1 o o
    0 o o
    X 0 1 2 3
    '''
    data = [
        Point(0,0), Point(0,1), 
        Point(1,0), Point(1,1),Point(23,42)
    ]

    print_example(data, prompt)