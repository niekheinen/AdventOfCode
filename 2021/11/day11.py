from itertools import product
import copy 

def flash(octopusses, x0, y0, flashers):
    flashers.add((x0, y0))
    for ax, ay in set(product([-1, 0, 1], repeat=2)):
        x1, y1 = x0 + ax, y0 + ay
        if x1 not in [-1, dim_x] and y1 not in [-1, dim_y] and (x1, y1) != (x0, y0):
            octopusses[y1][x1] += 1
            if octopusses[y1][x1] >= 10 and (x1, y1) not in flashers:
                octopusses, flashers = flash(octopusses, x1, y1, flashers)
    return octopusses, flashers

def puzzle1(octopusses):
    cnt = 0
    for _ in range(100):
        flashers = set()
        for y in range(dim_y):
            for x in range(dim_x):
                octopusses[y][x] += 1
                if octopusses[y][x] >= 10 and (x, y) not in flashers:
                    octopusses, flashers = flash(octopusses, x, y, flashers)
        
        for x, y in flashers:
            octopusses[y][x] = 0
            cnt += 1
    
    return cnt 

def puzzle2(octopusses):
    for i in range(10000):
        flashers = set()
        for y in range(dim_y):
            for x in range(dim_x):
                octopusses[y][x] += 1
                if octopusses[y][x] >= 10 and (x, y) not in flashers:
                    octopusses, flashers = flash(octopusses, x, y, flashers)
        
        for x, y in flashers:
            octopusses[y][x] = 0
    
        if all(all([i == 0 for i in line]) for line in octopusses):
            return i + 1

if __name__=='__main__':    
    with open('2021/11/input.txt') as f:
        lines = f.read().split('\n')

    dim_x, dim_y = len(lines[0]), len(lines)

    lines = [[int(i) for i in line] for line in lines]

    print(f'Puzzle 1 answer: {puzzle1(copy.deepcopy(lines))}')
    print(f'Puzzle 2 answer: {puzzle2(copy.deepcopy(lines))}')
    