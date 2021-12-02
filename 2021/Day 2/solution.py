class Postion():
    x = 0
    y = 0
    a = 0

    def forward(self, value):
        self.x += value

    def down(self, value):
        self.y += value

    def up(self, value):
        self.y -= value

    def aim(self, value):
        self.a += value

    def basic_move(self, command_tuple):
        command = command_tuple[0]
        value = command_tuple[1]

        if command == 'forward':
            self.forward(value)
        elif command == 'down':
            self.down(value)
        elif command == 'up':
            self.up(value)

    def advanced_move(self, command_tuple):
        command = command_tuple[0]
        value = command_tuple[1]

        if command == 'forward':
            self.forward(value)
            self.down(self.a*value)
        elif command == 'down':
            self.aim(value)
        elif command == 'up':
            self.aim(-value)

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

class Day():
    def __init__(self, data_path):
        self.data = self.data_parse(data_path)

    def data_parse(self, path): 
        data = open(path, "r")
        commands = []

        for line in data:
            split_line = line.strip().split(' ')
            command = (split_line[0], int(split_line[1]))
            commands.append(command)

        return commands

    def part1(self):
        position = Postion()
        for command in self.data:
            position.basic_move(command)

        return position.getX() * position.getY()

    def part2(self):
        position = Postion()
        for command in self.data:
            position.advanced_move(command)

        return position.getX() * position.getY()

        
if __name__ == "__main__":
    DATA_INPUT_LOCATION = "data.in"

    day = Day(DATA_INPUT_LOCATION)
    print(day.part1())
    print(day.part2())
