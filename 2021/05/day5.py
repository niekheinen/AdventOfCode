import re
from collections import Counter


# Dit moet in een lambda kunnen
def get_points(x1, y1, x2, y2, count_diagonal=False):
    if x1 == x2:
        return [(x1, y) for y in range(min(y1, y2), max(y1, y2)+1)] 
    elif y1 == y2:
        return [(x, y1) for x in range(min(x1, x2), max(x1, x2)+1)]
    elif count_diagonal:
        ax, ay = 1 if x2 >= x1 else -1, 1 if y2 >= y1 else -1
        return [i for i in zip(range(x1, x2 + ax, ax), range(y1, y2, ay))]
        

def puzzle1(lines):
    c = Counter()
    for line in lines:
        c.update(get_points(*line))
    return len([v for v in c.values() if v >= 2])


def puzzle2(lines):
    c = Counter()
    for line in lines:
        c.update(get_points(*line, count_diagonal=True))
    return len([v for v in c.values() if v >= 2])


if __name__=='__main__':
    with open('2021/05/input.txt') as file:
        lines = file.read().split('\n')
    lines = [list(map(int, re.split(' -> |,', line))) for line in lines]
    
    print(f'Puzzle 1 answer: {puzzle1(lines)}')
    print(f'Puzzle 2 answer: {puzzle2(lines)}')
    
