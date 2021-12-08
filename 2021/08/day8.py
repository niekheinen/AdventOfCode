def puzzle1(lines):
    count = 0
    for line in lines:
        for digit in line[1].split():
            if len(digit) in [2, 4, 3, 7]:
                count +=1
    return count


def subtract_digit(d1, d2):
    return [i for i in d1 if i not in d2]

def solve_digits(all_digits):
    len_to_digit = {
        2: 1,
        3: 7,
        4: 4,
        5: [2, 3, 5],
        6: [0, 6, 9],
        7: 8
    }

    digits = [None] * 10
    twothreefive = []
    zerosixnine = []

    for i in all_digits:
        d = len_to_digit[len(i)]
        if type(d) == int:
            digits[d] = i
        elif len(i) == 5:
            twothreefive.append(i)
        else:
            zerosixnine.append(i)
        
    for i in twothreefive:
        if len(subtract_digit(i, digits[1])) == 3:
            digits[3] = i
        elif len(subtract_digit(i, digits[4])) == 2:
            digits[5] = i
        else:
            digits[2] = i
    
    for i in zerosixnine:
        if len(subtract_digit(i, digits[1])) == 5:
            digits[6] = i
        elif len(subtract_digit(i, digits[4])) == 2:
            digits[9] = i
        else:
            digits[0] = i
    return digits

def get_digit(digits, digit):
    for g in digits:
        if set(g) == set(digit):
            return digits.index(g)


def puzzle2(lines):
    outputs = []
    for line in lines:
        digits = solve_digits(line[0].split())
        outputs.append(int(''.join([str(get_digit(digits, i)) for i in line[1].split()])))
    return sum(outputs)


if __name__=='__main__':
    with open('2021/08/input.txt') as file:
        lines = [i.split(' | ') for i in file.read().split('\n')]
        
    print(f'Puzzle 1 answer: {puzzle1(lines)}')
    print(f'Puzzle 2 answer: {puzzle2(lines)}')
