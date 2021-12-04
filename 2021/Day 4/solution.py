import numpy as np

class Bingo():
    def __init__(self):
        self.size = 5
        self.marked_numbers = []
        self.board = [[] for x in range(5)]

    def insert_board(self, board):
        self.board = board

    def clear(self):
        self.marked_numbers = []

    def check_horizontal(self):
        all = np.array(self.marked_numbers)
        for line in self.board:
            check = np.array(line)
            if np.all(np.isin(check, all)):
                return True
        return False
    
    def column(self, i):
        return [line[i] for line in self.board]

    def check_vertical(self):
        all = np.array(self.marked_numbers)
        for i in range(self.size):
            if np.all(np.isin(np.array(self.column(i)), all)):
                return True
        return False

    def check_winning(self, number):
        self.marked_numbers.append(number)
        if self.check_horizontal() or self.check_vertical():
            return True
        return False

    def score(self):
        sum = 0
        for line in self.board:
            for number in line:
                if number not in self.marked_numbers:
                    sum += number
        return sum

    def print_board(self):
        for line in self.board:
            for number in line:
                if number > 9:
                    print(number, end=' ')
                else:
                    print(' ', end='')
                    print(number, end=' ')
            print()

class Day():
    def __init__(self, data_path):
        self.numbers, self.bingos = self.data_parse(data_path)

    def data_parse(self, path): 
        numbers = []
        bingos = []
        with open(path, "r") as file:
            numbers = [int(number) for number in file.readline().strip().split(',')]
            board_lines = []

            iterator = 0
            for line in file:
                if line == '\n':
                    if bingos:
                        bingos[iterator].insert_board(board_lines)
                        board_lines = []
                        iterator += 1
                    bingos.append(Bingo())
                else:
                    board_lines.append([int(number) for number in line.strip().split()])
            # Append last board - EOF bypass
            bingos[iterator].insert_board(board_lines)

        return numbers, bingos

    def clear_marked_numbers(self):
        for bingo in self.bingos:
            bingo.clear()

    def part1(self):
        self.clear_marked_numbers()
        for number in self.numbers:
            for bingo in self.bingos:
                if bingo.check_winning(number):
                    return bingo.score() * number

    def part2(self):
        self.clear_marked_numbers()
        winned = []
        for number in self.numbers:
            for bingo in self.bingos:
                if bingo.check_winning(number):
                    if bingo not in winned:
                        winned.append(bingo)
                    if len(winned) == len(self.bingos):
                        return bingo.score() * number

if __name__ == "__main__":
    DATA_INPUT_LOCATION = "data.in"

    day = Day(DATA_INPUT_LOCATION)
    print(day.part1())
    print(day.part2())
