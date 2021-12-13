def fold(dots, fold):
    ret = set()
    for dot in dots:
        if fold[0] == 'x':
            ret.add((fold[1] - abs(dot[0] - fold[1]), dot[1]))
        else:
            ret.add((dot[0], fold[1] - abs(dot[1] - fold[1]),))
    return ret

def puzzle1(dots, folds):
    return len(fold(dots, folds[0]))

def puzzle2(dots, folds):
    for f in folds:
        dots = fold(dots, f)
    dim_x, dim_y = max([dot[0] for dot in dots]), max([dot[1] for dot in dots])
    for y in range(dim_y + 1):
        print(''.join(['#' if (x, y) in dots else ' ' for x in range(dim_x + 1)]))


if __name__=='__main__':
    with open('2021/13/input.txt') as f:
        dots, folds = f.read().split('\n\n')
    
    parse_dot = lambda a: (int(a[0]), int(a[1]))
    dots = [parse_dot(dot.split(',')) for dot in dots.split('\n')]
    
    parse_fold = lambda a: (a[0][-1], int(a[1]))
    folds = [parse_fold(fold.split('=')) for fold in folds.split('\n')]

    print(f'Puzzle 1 answer: {puzzle1(dots, folds)}')
    print(f'Puzzle 2 answer: {puzzle2(dots, folds)}')