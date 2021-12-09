from typing import DefaultDict


class Day():
    def __init__(self, data_path):
        self.data = DefaultDict()

        with open(data_path, "r") as file:
            for row, line in enumerate(file):
                for col, number in enumerate(line.strip()):
                    self.data[(row, col)] = int(number)
            
        self.rows = max(self.data.keys())[0]
        self.cols = max(self.data.keys())[1]

    def get_neighbors(self, coordinates):
        neighbors = []
        
        if coordinates[0] < self.rows:                              # Bottom border check
            neighbors.append((coordinates[0] + 1, coordinates[1]))
        if coordinates[0] > 0:                                      # Top border check
            neighbors.append((coordinates[0] - 1, coordinates[1]))
        if coordinates[1] < self.cols:                              # Right border check
            neighbors.append((coordinates[0], coordinates[1] + 1))
        if coordinates[1] > 0:                                      # Left border check
            neighbors.append((coordinates[0], coordinates[1] - 1))
        
        return neighbors

    def part1(self):
        sum = 0

        for point in self.data:
            is_minimum = True
            for neighbor in self.get_neighbors(point):
                if self.data[point] >= self.data[neighbor]:
                    is_minimum = False
                    break
            if is_minimum:
                sum += 1 + self.data[point]

        return sum

    def get_basin(self, point, visited):
        size = 1

        for neighbor in self.get_neighbors(point):
            if neighbor not in visited:
                visited.append(neighbor)
                if self.data[neighbor] != 9:
                    size += self.get_basin(neighbor, visited)

        return size


    def part2(self):
        sizes = []
        visited = []

        for point in self.data:
            is_minimum = True
            for neighbor in self.get_neighbors(point):
                if self.data[point] >= self.data[neighbor]:
                    is_minimum = False
                    break
            if is_minimum:
                visited.append(point)
                sizes.append(self.get_basin(point, visited))
        
        sizes.sort()

        return sizes[-3] * sizes[-2] * sizes[-1]
            


if __name__ == "__main__":
    DATA_INPUT_LOCATION = "data.in"

    day = Day(DATA_INPUT_LOCATION)
    print(day.part1())
    print(day.part2())