def puzzle1(lines):
    points = 0
    close_table = {')': '(', ']': '[', '}': '{', '>': '<'}
    point_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
    for line in lines:
        s = ''
        for c in line:
            if c in '([{<':
                s += c
            elif close_table[c] == s[-1]:
                s = s[:-1]
            else:
                points += point_table[c]
                break
    return points

def puzzle2(lines):
    scores = []
    close_table = {')': '(', ']': '[', '}': '{', '>': '<'}
    score_table = {'(': 1, '[': 2, '{': 3, '<': 4}
    for line in lines:
        score, s = 0, ''
        for c in line:
            if c in '([{<':
                s += c
            elif close_table[c] == s[-1]:
                s = s[:-1]
            else:
                s = ''
                break
        
        if s != '':
            [(score := score * 5 + score_table[x]) for x in reversed(s)]
            scores.append(score)

    return sorted(scores)[len(scores)//2]


if __name__=='__main__':
    with open('2021/10/input.txt') as f:
        lines = f.read().split('\n')

    print(f'Puzzle 1 answer: {puzzle1(lines)}')
    print(f'Puzzle 2 answer: {puzzle2(lines)}')