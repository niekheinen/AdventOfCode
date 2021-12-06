def new_day(fish):
    fish = [f - 1 for f in fish]
    return [6 if f == -1 else f for f in fish] + [8] * fish.count(-1)

def puzzle1(fish):
    for _ in range(80):
        fish = new_day(fish) 
    return len(fish)


def puzzle2(fish):
    c = [0] * 9
    for f in fish:
        c[f] += 1
    for _ in range(256):
        new = c.pop(0)
        c[6] += new
        c.append(new)
    return sum(c)


def golf():
    c, t = [0] * 9, lambda l: ((n:=l[0]), [n + v if i == 6 else v for i, v in enumerate(l[1:])] + [n])    
    for f in [int(i) for i in open('2021/06/input.txt').read().split(',')]: c[f] += 1
    for _ in range(256): c = t(c)[1]
    print(sum(c))

if __name__=='__main__':
    with open('2021/06/input.txt') as file:
        lines = [int(i) for i in file.read().split(',')]
        
    print(f'Puzzle 1 answer: {puzzle1(lines)}')
    print(f'Puzzle 2 answer: {puzzle2(lines)}')

    golf() 