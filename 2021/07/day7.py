def puzzle1(lines):
    return min([sum([abs(j - i) for j in lines]) for i in range(max(lines))])

def puzzle2(lines):
    e = lambda d: int((d + 1) * d/2)
    return min([sum([e(abs(j - i)) for j in lines]) for i in range(max(lines))])

if __name__=='__main__':
    with open('2021/07/input.txt') as file:
        lines = [int(i) for i in file.read().split(',')]

    print(f'Puzzle 1 answer: {puzzle1(lines)}')
    print(f'Puzzle 2 answer: {puzzle2(lines)}')
