def puzzle1():
    with open('2021/03/input.txt') as file:
        lines = file.read().split('\n')
        counter = [0] * (bits := len(lines[0]))
        
        for line in lines: 
            for i in range(bits):
                counter[i] += int(line[i])
        
        gamma = int(''.join(['1' if count >= (len(lines) / 2) else '0' for count in counter]), 2)
        return gamma * (gamma ^ int('1' * bits, 2))


def puzzle1_golf():
    l = open('2021/03/input.txt').read().split('\n')
    c = [0] * (b := len(l[0]))
    for n in l: c = map(sum, zip(c, [int(i) for i in n]))
    g = int(''.join([str(int(i >= (len(l) / 2))) for i in c]), 2)
    print(g * (g ^ int('1' * b, 2)))


# Dit kan ongetwijveld mooier, maar copy-paste is soms ook nice :)
def puzzle2():
    with open('2021/03/input.txt') as file:
        lines = file.read().split('\n')

    def most_common_bit(lines, bit_index):
        return int(sum([int(line[bit_index]) for line in lines]) >= len(lines) / 2)
    
    def get_o(lines):
        for i in range(len(lines)):
            if len(lines) == 1:
                return int(lines[0], 2)
            lines = [line for line in lines if int(line[i]) == most_common_bit(lines, i)]
    
    def get_co2(lines):
        for i in range(len(lines)):
            if len(lines) == 1:
                return int(lines[0], 2)
            lines = [line for line in lines if not int(line[i]) == most_common_bit(lines, i)]

    return get_o(lines) * get_co2(lines)

if __name__=='__main__':
    print(f'Puzzle 1 answer: {puzzle1()}')
    puzzle1_golf()
    print(f'Puzzle 2 answer: {puzzle2()}')