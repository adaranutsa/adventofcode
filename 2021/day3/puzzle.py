import sys

def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def puzzle1(data):
    """
    Input data should be sanitized.

    The function should return the result.
    """

    # gamma_rate = most common num in a row. Convert binary to decimal.
    # epsilon_rate = least common num in a row. Convert binary to decimal.

    data_set = {}
    gamma_rate = ""
    epsilon_rate = ""

    for line in data:
        for index, num in enumerate(line.strip()):
            if index in data_set:
                data_set[index].append(num)
            else:
                data_set[index] = [num]

    for x in range(0,len(data_set)):
        gamma_rate += max(set(data_set[x]), key=data_set[x].count)
        epsilon_rate += min(set(data_set[x]), key=data_set[x].count)

    power_consumption = binaryToDecimal(int(gamma_rate)) * binaryToDecimal(int(epsilon_rate))

    return power_consumption

def get_rating(data, bit=0, ox=True):
    orig_data = data.copy()
    count_0 = 0
    count_1 = 0

    for d in orig_data:
        if d[bit] == "0":
            count_0 += 1
        else:
            count_1 += 1

    if ox:
        max_num = "0" if count_0 > count_1 else "1"
    else:
        max_num = "0" if count_0 <= count_1 else "1"

    remove = []
    for d in orig_data:
        if not d[bit] == max_num:
            remove.append(d)

    for r in remove:
        orig_data.remove(r)

    if len(orig_data) != 1:
        return get_rating(orig_data, bit+1, ox)
    
    return orig_data[0]

def puzzle2(data):
    """
    Input data should be sanitized.

    The function should return the result.
    """

    ox_rating = int(get_rating(data))
    co2_rating = int(get_rating(data, ox=False))

    return binaryToDecimal(ox_rating) * binaryToDecimal(co2_rating)

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