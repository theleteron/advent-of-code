class Day():
    def __init__(self, data_path):
        with open(data_path, "r") as file:
            for line in file:
                self.instructions = line.strip()

    def part1(self):
        floor = 0
        for char in self.instructions:
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1
        
        return floor


    def part2(self):
        floor = 0
        instruction = 1
        for char in self.instructions:
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1
            if floor < 0:
                return instruction
            instruction += 1

        return -1


if __name__ == "__main__":
    DATA_INPUT_LOCATION = "data.in"

    day = Day(DATA_INPUT_LOCATION)
    print(day.part1())
    print(day.part2())