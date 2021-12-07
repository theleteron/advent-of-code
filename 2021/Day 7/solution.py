class Day():
    def __init__(self, data_path):
        with open(data_path, "r") as file:
            for line in file:
                self.positions = [(int(position)) for position in line.strip().split(',')]

    def part1(self):
        fuel_cost = -1

        for target in range(min(self.positions), max(self.positions)+1):
            current_cost = 0
            for number in self.positions:
                current_cost += target - number if target > number else number - target
            if current_cost < fuel_cost or fuel_cost == -1:
                fuel_cost = current_cost
        
        return fuel_cost

    def cost(self, x):
        return x * (x + 1) // 2

    def part2(self):
        fuel_cost = -1

        for target in range(min(self.positions), max(self.positions)+1):
            current_cost = 0
            for number in self.positions:
                current_cost += self.cost(target - number) if target > number else self.cost(number - target)
            if current_cost < fuel_cost or fuel_cost == -1:
                fuel_cost = current_cost
        
        return fuel_cost

if __name__ == "__main__":
    DATA_INPUT_LOCATION = "data.in"

    day = Day(DATA_INPUT_LOCATION)
    print(day.part1())
    print(day.part2())