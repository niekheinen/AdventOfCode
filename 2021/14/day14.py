from collections import Counter

def puzzle1(polymer, pairs):
    for _ in range(10):
        new_polymer = ''
        for i in range(len(polymer) - 1):
            new_polymer += polymer[i] + pairs[polymer[i:i+2]]
        polymer = new_polymer + polymer[i+1]
    
    c = Counter(polymer)
    return c.most_common(1)[0][1] - c.most_common()[-1][1]

def puzzle2(polymer, pairs):
    c = Counter(polymer)
    pair_count = Counter([polymer[i:i+2] for i in range(len(polymer)-1)])
    for _ in range(40):
        new_pair_count = Counter()
        for k, v in pair_count.items():
            e = pairs[k]
            c.update({e: v})
            new_pair_count.update({k[0] + e: v, e + k[1]: v})
        pair_count = new_pair_count
    return c.most_common(1)[0][1] - c.most_common()[-1][1]
    

if __name__=='__main__':
    with open('2021/14/input.txt') as f:
        polymer, pairs = f.read().split('\n\n')

    pairs = {p[:2]: p[-1] for p in pairs.split('\n')}

    print(f'Puzzle 1 answer: {puzzle1(polymer, pairs)}')
    print(f'Puzzle 2 answer: {puzzle2(polymer, pairs)}')