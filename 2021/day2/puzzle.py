import sys

def get_int(obj):
    return int(obj.split(" ")[1].strip())

def puzzle1(data, p2=False):
    """
    Input data should be sanitized.

    The function should return the result.
    """
    hor_pos = 0
    dep_pos = 0
    aim = 0

    for d in data:
        if 'forward' in d:
            hor_pos += get_int(d)

            if hor_pos != 0:
                dep_pos += get_int(d) * aim

        if 'down' in d:
            if not p2:
                dep_pos += get_int(d)
            else:
                aim += get_int(d)

        if 'up' in d:
            if not p2:
                dep_pos -= get_int(d)
            else:
                aim -= get_int(d)

    return hor_pos * dep_pos

def puzzle2(data):
    """
    Input data should be sanitized.

    The function should return the result.
    """
    return puzzle1(data, p2=True)

def is_test():
    return True if '-t' in sys.argv else False

if __name__ == '__main__':
    test = is_test()

    test_input = 'puzzle.test.txt'
    real_input = 'puzzle.input.txt'

    if not test:
        data_input = real_input
        msg = "Puzzle"
    else:
        data_input = test_input
        msg = "Test Puzzle"

    with open(data_input, 'r') as f:
        data = f.readlines()

        # TODO: Sanitize data into proper format. This could be int or simply removing the newlines.
        #data = [int(x.strip()) for x in data]

    if '-p1' in sys.argv:
        p1_out = puzzle1(data)
        print(f"{msg} 1 Output: {p1_out}")

    if '-p2' in sys.argv:
        p2_out = puzzle2(data)
        print(f"{msg} 2 Output: {p2_out}")