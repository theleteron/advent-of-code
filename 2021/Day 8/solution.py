'''
0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

1 : 2 - unique
7 : 3 - unique
4 : 4 - unique
2 : 5 - intersects in 2 points with '4'
3 : 5 - '1' is in it
5 : 5 - intersects in 3 points with '4'
0 : 6 - '1' is in it
6 : 6 
9 : 6 - '4' is in it and '1' is in it
8 : 7 - unique
'''

class Day():
    sorted = False

    def __init__(self, data_path):
        with open(data_path, "r") as file:
            self.data = file.readlines()

    def sort(self):
        if self.sorted:
            return
        self.sorted = True
        self.observations = []
        self.outputs = []

        for line in self.data:
            self.observations.append(["".join(sorted(value)) for value in line.strip().split('|')[0].split()])
            self.outputs.append(["".join(sorted(value)) for value in line.strip().split('|')[1].split()])

    def get_known_digits(self, observation):
        digits = {0 : '', 1 : '', 2 : '', 3 : '', 4 : '', 5 : '', 6 : '', 7 : ''}
        for value in observation:
            if len(value) == 2:
                digits[1] = value
            elif len(value) == 4:
                digits[4] = value
            elif len(value) == 3:
                digits[7] = value
            elif len(value) == 7:
                digits[8] = value
        return digits

    def part1(self):
        self.sort()
        count = 0
        for i, observation in enumerate(self.observations):
            digits = self.get_known_digits(observation)
            for value in self.outputs[i]:
                if value in digits.values():
                    count += 1
        return count

    def intersection(self, string1, string2):
        count = 0
        for char in string1:
            if char in string2:
                count += 1
        return count

    def get_all_digits(self, observation):
        digits = self.get_known_digits(observation)
        for value in observation:
            length = len(value)
            if length == 5 and self.intersection(value, digits[1]) == 2:
                digits[3] = value
            elif length == 5 and self.intersection(value, digits[4]) == 2:
                digits[2] = value
            elif length == 5 and self.intersection(value, digits[4]) == 3:
                digits[5] = value
            elif length == 6 and self.intersection(value, digits[1]) == 2 and self.intersection(value, digits[4]) == 4:
                digits[9] = value
            elif length == 6 and self.intersection(value, digits[1]) == 2:
                digits[0] = value
            elif length == 6:
                digits[6] = value
        return digits

    def part2(self):
        self.sort()
        sum = 0
        for i, observation in enumerate(self.observations):
            digits = self.get_all_digits(observation)
            output_number = []
            for value in self.outputs[i]:
                output_number.append(str(list(digits.keys())[list(digits.values()).index(value)]))
            sum += int("".join(output_number))
        return sum
if __name__ == "__main__":
    DATA_INPUT_LOCATION = "data.in"

    day = Day(DATA_INPUT_LOCATION)
    print(day.part1())
    print(day.part2())