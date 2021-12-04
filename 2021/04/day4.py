class Board():
    def __init__(self, board_text): 
        self.board = [[0 for _ in range(5)] for _ in range(5)]
        for i, n in enumerate(board_text.replace('\n', ' ').split()):
            self.board[i % 5][i // 5] = int(n)

    def call_num(self, num):
        self.board = [['x' if n == num else n for n in col] for col in self.board]
        for i in range(5):
            if self.board[i] == ['x'] * 5 or [col[i] for col in self.board] == ['x'] * 5:
                return self.sum_unmarked() * num
        return False

    def sum_unmarked(self):
        temp = []
        for col in self.board:
            temp += col
        return sum(n for n in temp if n != 'x')




def puzzle1(lines, numbers):
    boards = [Board(line) for line in lines]
    for n in numbers:
        for b in boards:
            if (score := b.call_num(n)):
                return score


def puzzle2(lines, numbers):
    boards = [Board(line) for line in lines]
    for n in numbers:
        boards = [b for b in boards if not (score := b.call_num(n))]
    return score


def puzzle1_golf():
    f = '2021/04/input.txt'
    l = open(f).read().split('\n\n')
    nums = [int(n) for n in l.pop(0).split(',')]
    j = 0
    callnum = lambda board, call: board.replace(call, f)
    haswon = lambda board : 0
    calcscore = lambda board, call: sum(n for n in board if n!=f) * call if haswon(board) else 0
    
    
    while (score := max([callscore(b) for b in boards])) == 0:
        boards = [i.replace(nums.pop(0), f) for i in boards]
    print(score)

    scores = [[i * b.replace('\n', ' ').split() for i in n] for b in l]
    


    def call_num(board, num):
        board = [['x' if n == num else n for n in col] for col in board]
        for i in range(5):
            if board[i] == ['x'] * 5 or [col[i] for col in board] == ['x'] * 5:
                return sum_unmarked() * num
        return False

    def sum_unmarked(board):
        temp = []
        for col in board:
            temp += col
        return sum(n for n in temp if n != 'x')
    return 0

if __name__=='__main__':
    with open('2021/04/input.txt') as file:
        lines = file.read().split('\n\n')    

    numbers = [int(n) for n in lines.pop(0).split(',')]
   
    print(f'Puzzle 1 answer: {(ans1 := puzzle1(lines, numbers))}')
    print(f'Puzzle 2 answer: {puzzle2(lines, numbers)}')
    
    assert ans1 == 35711
    #assert ans1 == puzzle1_golf()
