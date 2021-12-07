from collections import Counter, defaultdict

class Lanterfish():
    def __init__(self, days=8):
        self.days_till_spawn = days            # Days till spawning new lanterfish
    
    def spawn(self):
        if self.days_till_spawn == 0:
            self.days_till_spawn = 6
            return True
        else:
            self.days_till_spawn -= 1
            return False
    
    def __str__(self):
        return str(self.days_till_spawn)

class Day():
    def __init__(self, data_path):
        with open(data_path, "r") as file:
            for line in file:
                self.initial_lanternfishes = [Lanterfish(int(days)) for days in line.strip().split(',')]
                self.counter = Counter(map(int, line.strip().split(',')))

    def part1(self, days):
        lanternfishes = self.initial_lanternfishes
        lenght = 0
        for day in range(days+1):
            lenght = len(lanternfishes)
            for i in range(lenght):
                if lanternfishes[i].spawn():
                    lanternfishes.append(Lanterfish())                  # Spawn already for a next day (have to take lenght of array before this point)
        return lenght

    def part2(self, days):
        # Using dictionary idea https://github.com/mebeim/aoc/blob/master/2021/solutions/day06.py
        for _ in range(days):
            newborn = defaultdict(int)

            for d, fish in self.counter.items():
                d -= 1

                if d < 0:
                    newborn[6] += fish
                    newborn[8] += fish
                else:
                    newborn[d] += fish
                
            self.counter = newborn
        
        return sum(self.counter.values())

if __name__ == "__main__":
    DATA_INPUT_LOCATION = "data.in"
    SIMULATION_LENGTH_P1 = 80
    SIMULATION_LENGTH_P2 = 256

    day = Day(DATA_INPUT_LOCATION)
    print(day.part1(SIMULATION_LENGTH_P1))
    print(day.part2(SIMULATION_LENGTH_P2))