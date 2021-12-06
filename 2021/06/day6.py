from collections import Counter

def new_day(fish):
    fish = [f - 1 for f in fish]
    return [6 if f == -1 else f for f in fish] + [8] * fish.count(-1)

def puzzle1(fish):
    for _ in range(80):
        fish = new_day(fish) 
    return len(fish)


def puzzle2(fish):
    c = list(zip(range(9), [0] * 9))
    count = Counter(fish)
    c = [[k, count[k] if k in count.keys() else v] for k, v in c]
    ret = sum(count.values())
    for _ in range(256):
        new = c[0][1]
        c = [[k - 1, v] for k, v in c]
        del c[0]
        c[6][1] += new
        c.append([8, new])
        ret += new
    return ret


if __name__=='__main__':
    with open('2021/06/input.txt') as file:
        lines = [int(i) for i in file.read().split(',')]
        
    print(f'Puzzle 1 answer: {puzzle1(lines)}')


    print(f'Puzzle 2 answer: {puzzle2(lines)}')
    
