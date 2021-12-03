def puzzle1():
    x, y = 0, 0
    v = {'forward': [1, 0], 'up':[0, -1], 'down': [0, 1]}
    with open('day2/input.txt') as file:
        for line in file.readlines():
            command, amount = line.strip().split()
            amount = int(amount)
            x += v[command][0] * amount
            y += v[command][1] * amount 
    return x * y

def puzzle2():
    h, d, a = 0, 0, 0
    with open('day2/input.txt') as file:
        for line in file.readlines():
            command, amount = line.strip().split()
            amount = int(amount)
            if command == 'forward':
                h += amount
                d += a * amount
            elif command == 'up':
                a -= amount
            elif command == 'down':
                a += amount
    return h * d

if __name__=='__main__':
    print(f'Puzzle 1 answer: {puzzle1()}')
    print(f'Puzzle 2 answer: {puzzle2()}')