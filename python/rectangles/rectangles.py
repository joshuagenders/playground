from itertools import permutations

def traverse_array(input_arr, starting, finishing, levels):
    if levels > 1:
        for x in range(starting, finishing - (levels - 1)):
            for nxt in traverse_array(input_arr, x + 1, finishing, levels - 1):
                y = [input_arr[x]] + nxt
                if len(y) >= 4:
                    print (",".join([str(input_arr.index(o)) for o in y]))
                yield [input_arr[x]] + nxt
    if levels <= 1:
        for current in range(starting + levels - 1, finishing):
            yield [input_arr[current]]

def traverse_array_2(input_arr, starting, finishing, levels):
    positions = [i + starting for i in range(levels)]
    while positions[0] < finishing - levels:
        yield output_arr(input_arr, positions)
        increment_indexes(positions, finishing)

def increment_indexes(positions, end):
    max_positions = [end - i for i in range(len(positions), -1, -1)]
    last_marker_index = len(positions) - 1
    incremented_marker = None
    for marker in range(last_marker_index, -1, -1):
        current_marker_position = positions[marker]
        if current_marker_position < max_positions[marker]:
            positions[marker] += 1
            incremented_marker = marker
            break
    if not incremented_marker: #reached all max positions
        return
    for marker in range(incremented_marker + 1, last_marker_index + 1):
        positions[marker] = positions[incremented_marker] + (marker - incremented_marker)

def output_arr(input_arr, current_positions):
    output = [input_arr[current_positions[i]] for i in range(len(current_positions))]
    msg = ";".join([str(o) for o in output])
    print (f"{current_positions} {msg}")
    return output

def unique_permutations_of_length(input_arr, length):
    unique_list = list(set(input_arr))
    return traverse_array(unique_list, 0, len(unique_list), length)

def is_rectangle(p1, p2, p3, p4):
    # ((x, y),(x1, y1),(x, y1),(x1, y))
    is_rectangle = True
    is_rectangle &= p1.x == p3.x 
    is_rectangle &= p1.y == p4.y 
    is_rectangle &= p2.x == p4.x
    is_rectangle &= p2.y == p3.y
    return is_rectangle

def any_permutations_are_rectangle(p1,p2,p3,p4):
    for p in permutations([p1,p2,p3,p4]):
        if is_rectangle(p[0],p[1],p[2],p[3]):
            return True
    return False

def try_join(p1, p2):
    if p1.x == p2.x:
        return (True, 'y')
    if p1.y == p2.y:
        return (True, 'x')
    return (False, None)

def count_rectangles_2(points):
    point_permutations = [[p, is_rectangle_2(p[0], p[1], p[2], p[3])] for p in unique_permutations_of_length(points, 4)]
    rect_permutations = filter(lambda p: p[1], point_permutations)
    return len(list(rect_permutations))

def is_rectangle_2(p1,p2,p3,p4):
    r1 = p1
    r2 = None
    r3 = None
    r4 = None
    points = [p2,p3,p4]
    for p in points:
        r = try_join(r1, p)
        if (r[0]):
            r2 = p
            next = r[1]
            break
    if r2:
        points.remove(r2)
    else:
        return False # no joining point found
    for p in points:
        if getattr(p, next) == getattr(r2, next):
            r3 = p
            next = 'x' if next == 'y' else 'y'
            break
    if r3:
        points.remove(r3)
    else:
        return False

    r4 = points[0]
    opposite = 'x' if next == 'y' else 'y'
    if getattr(r4, next) == getattr(r3, next) and getattr(r4, opposite) == getattr(r1, opposite):
        return True
    return False

def count_rectangles(points):
    point_permutations = [[p, any_permutations_are_rectangle(p[0], p[1], p[2], p[3])] for p in unique_permutations_of_length(points, 4)]
    rect_permutations = filter(lambda p: p[1], point_permutations)
    return len(list(rect_permutations))

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
    def try_join(self, point):
        if not self.joined_x:
            if point.x == self.x:
                self.joined_x = point
                return True
        if not self.joined_y:
            if point.y == self.y:
                self.joined_y = point
                return True
        return False       
    def is_fully_joined(self):
        return self.joined_x and self.joined_y

def print_example(data, prompt):
    print(prompt)
    print(f"Number of rectangles is {count_rectangles(data)}")
    print(f"Number of rectangles(2) is {count_rectangles_2(data)}")

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