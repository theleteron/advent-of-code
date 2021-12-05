class Map():
    def __init__(self, data, size, diagonal):
        self.map = [[0 for y in range(size)] for x in range(size)]
        self.fill_map(data, diagonal)

    def fill_map(self, data, diagonal):
        for coordinates in data:
            self.fill_line(coordinates, diagonal)

    def fill_line(self, coordinates, allow_diagonal):
        start_x, start_y = coordinates[0][0], coordinates[0][1]
        end_x, end_y = coordinates[1][0], coordinates[1][1]
        
        if (start_x != end_x and start_y != end_y) and not allow_diagonal: # No diagonals
            pass 

        elif (start_x != end_x and start_y != end_y) and allow_diagonal:   # Diagonals
            if start_x < end_x and start_y < end_y:     # Top left to bottom right
                i = 0
                for y in range(start_y, end_y+1):
                    self.map[y][start_x+i] += 1
                    i += 1
            elif start_x > end_x and start_y < end_y:   # Top right to bottom left
                i = 0
                for y in range(start_y, end_y+1):
                    self.map[y][start_x-i] += 1
                    i += 1
            elif start_x > end_x and start_y > end_y:   # Bottom right to top left
                i = 0
                for y in range(start_y, end_y-1, -1):
                    self.map[y][start_x-i] += 1
                    i += 1
            else:                                       # Bottom left to top right
                i = 0
                for y in range(start_y, end_y-1, -1):
                    self.map[y][start_x+i] += 1
                    i += 1
        
        elif start_x != end_x:                      # Horizontal
            for x in range(start_x if start_x < end_x else end_x, end_x+1 if start_x < end_x else start_x+1):
                self.map[start_y][x] += 1

        else:                                       # Vertical
            for y in range(start_y if start_y < end_y else end_y, end_y+1 if start_y < end_y else start_y+1):
                self.map[y][start_x] += 1

    def intersections(self):
        intersection = 0

        for line in self.map:
            for number in line:
                if number > 1:
                    intersection += 1
        
        return intersection

    def print_map(self):
        print("  ##### Printout of the Map #####  ")
        for line in self.map:
            print('\t', end='')
            for number in line:
                print(number, end=' ')
            print()
        print("  ###############################  ")


    
class Day():
    def __init__(self, data_path):
        self.data, self.size = self.data_parse(data_path)

    def data_parse(self, path):
        points = []
        size = 0
        with open(path, "r") as file:
            for line in file:
                points.append([tuple(int(n) for n in c.split(',')) for c in line.strip().split(' -> ')])

        for coordinates in points:
            for point in coordinates:
                for number in point:
                    if number > size:
                        size = number

        return points, size+1

    def part1(self):
        self.map = Map(self.data, self.size, False)
        return self.map.intersections()

    def part2(self):
        self.map = Map(self.data, self.size, True)
        return self.map.intersections()

if __name__ == "__main__":
    DATA_INPUT_LOCATION = "data.in"

    day = Day(DATA_INPUT_LOCATION)
    print(day.part1())
    print(day.part2())