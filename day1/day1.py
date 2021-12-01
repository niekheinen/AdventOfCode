def parse_measurements(file_name):
    with open(file_name) as f:
        return [int(line.strip()) for line in f.readlines()]

def puzzle1(measurements):
    return sum([1 if measurements[i] > measurements[i - 1] else 0 for i in range(1, len(measurements))])

def puzzle2(measurements, window_size=3):
    return puzzle1([sum(measurements[i:i+window_size]) for i in range(len(measurements) - window_size + 1)])

if __name__=='__main__':
    measurements = parse_measurements('day1/input1.txt')
    print(f'Puzzle 1 answer: {puzzle1(measurements)}')
    print(f'Puzzle 2 answer: {puzzle2(measurements)}')
