from itertools import permutations

def is_rectangle(p1, p2, p3, p4):
    # ((x, y),(x1, y1),(x, y1),(x1, y))
    return p1.x == p3.x and p1.y == p4.y and p2.x == p4.x and p2.y == p3.y

def any_permutations_are_rectangle(p1,p2,p3,p4):
    for p in permutations([p1,p2,p3,p4]):
        if is_rectangle(p[0],p[1],p[2],p[3]):
            return True
    return False

def count_rectangles(points):
    point_permutations = [[p, any_permutations_are_rectangle(p[0], p[1], p[2], p[3])] for p in permutations(points, 4)]
    rect_permutations = filter(lambda p: p[1], point_permutations)
    # todo do unique earlier
    unique_permutations = set(map(lambda p : tuple(sorted(map(str, p[0]))), rect_permutations))
    print(*unique_permutations, sep='\n')
    return len(list(unique_permutations))

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