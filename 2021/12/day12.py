def find_edges(edges, start):
    return [edge if edge[0] == start else edge[::-1] for edge in edges if start in edge]

def puzzle1(edges):
    paths = set([('start',)])
    while not all([p[-1] == 'end' for p in paths]):
        new_paths = set()
        for p in paths:
            if p[-1] == 'end':
                new_paths.add(p)
                continue

            for e in find_edges(edges, p[-1]):
                if e[1].isupper() or e[1] not in p:
                    new_paths.add((*p, e[1]))
        
        paths = new_paths
    # [print(p) for p in paths]
    return len(paths)


def allow_second_visit(path, small_cave):
    if small_cave == 'start':
        return False
    return max([path.count(cave) for cave in path if cave.islower() and cave != 'start']) < 2

def puzzle2(edges):
    paths = set([('start',)])
    while not all([p[-1] == 'end' for p in paths]):
        new_paths = set()
        for p in paths:
            if p[-1] == 'end':
                new_paths.add(p)
                continue

            for e in find_edges(edges, p[-1]):
                if e[1].isupper() or e[1] not in p or allow_second_visit(p, e[1]):
                    new_paths.add((*p, e[1]))
        
        paths = new_paths
    # [print(p) for p in paths]
    return len(paths)

if __name__=='__main__':
    with open('2021/12/input.txt') as f:
        edges = [tuple(line.split('-')) for line in f.read().split('\n')]



    #print(f'Puzzle 1 answer: {puzzle1(edges)}')
    print(f'Puzzle 2 answer: {puzzle2(edges)}')