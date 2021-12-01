import sys

def puzzle1(data):
    last_num = data[0]
    count = 0

    for d in data[1:]:
        if d > last_num:
            count += 1
        last_num = d

    return count

def puzzle2(data):

    p1 = 0
    p2 = 1
    p3 = 2

    summed_set = []

    while p3 < len(data):
        summed_set.append(
            data[p1] + data[p2] + data[p3]
        )

        p1 += 1
        p2 += 1
        p3 += 1

    return puzzle1(summed_set)

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
        data = [int(x.strip()) for x in data]

    if '-p1' in sys.argv:
        p1_out = puzzle1(data)
        print(f"{msg} 1 Output: {p1_out}")

    if '-p2' in sys.argv:
        p2_out = puzzle2(data)
        print(f"{msg} 2 Output: {p2_out}")