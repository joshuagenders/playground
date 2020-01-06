from itertools import permutations

def traverse_array(input_arr, starting, finishing, levels):
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