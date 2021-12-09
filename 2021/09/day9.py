def get_adjecents(x, y):
    adjecents = [] # adjecents = [up, right, down, left]
    adjecents.append((x, y-1) if y != 0 else None) 
    adjecents.append((x+1, y) if x != dim_x - 1 else None) 
    adjecents.append((x, y+1) if y != dim_y - 1 else None) 
    adjecents.append((x-1, y) if x != 0 else None)
    return adjecents


def puzzle1(lines):
    risklevel = 0
    for y, line in enumerate(lines):
        for x, point in enumerate(list(line)):
            if all([a is None or point < lines[a[1]][a[0]] for a in get_adjecents(x, y)]):
                risklevel += int(point) + 1
    return risklevel


def get_basin_size(low_point, lines):
    basin = set([low_point])
    explore = set(get_adjecents(*low_point))
    while len(explore) > 0:
        temp = set()
        for i in explore:
            if i is not None and int(lines[i[1]][i[0]]) != 9:
                basin.add(i)
                temp.update(get_adjecents(*i))
        explore = temp - basin
    return len(basin)


def puzzle2(lines):
    basins = []
    for y, line in enumerate(lines):
        for x, point in enumerate(list(line)):
            if all([a is None or point < lines[a[1]][a[0]] for a in get_adjecents(x, y)]):
                basins.append(get_basin_size((x, y), lines))
    ret = 1
    for i in sorted(basins, reverse=True)[:3]:
        ret = ret * i
    return ret


if __name__=='__main__':
    with open('2021/09/input.txt') as f:
        lines = f.read().split('\n')

    dim_y, dim_x = len(lines), len(lines[0])

    print(f'Puzzle 1 answer: {puzzle1(lines)}')
    print(f'Puzzle 2 answer: {puzzle2(lines)}')