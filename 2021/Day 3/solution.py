class Day():
    def __init__(self, data_path):
        self.data = self.data_parse(data_path)
        self.data_len = len(self.data[0])

    def data_parse(self, path): 
        data = open(path, "r")
        bits = []

        for line in data:
            bits.append(line.strip())

        return bits

    def most_common(self, i, data=None):
        ones = 0
        zeros = 0
        for bits in self.data if data is None else data:
            if int(bits[i]):
                ones += 1
            else:
                zeros += 1
        
        return 1 if ones >= zeros else 0

    def least_common(self, i, data=None):
        ones = 0
        zeros = 0
        for bits in self.data if data is None else data:
            if int(bits[i]):
                ones += 1
            else:
                zeros += 1
        
        return 1 if ones < zeros else 0

    def part1(self):
        mst_common = []
        lst_common = []
        for i in range(self.data_len):
            mst_common.append(str(self.most_common(i)))
            lst_common.append(str(self.least_common(i)))
        return int(''.join(mst_common), 2) * int(''.join(lst_common), 2)

    def oxygen_generator(self):
        values = [[] for i in range(self.data_len)]
        for i in range(self.data_len):
            if len(values[i-1]) == 1:
                return int(values[i-1][0], 2)
            deciding = self.most_common(i, values[i-1] if i > 0 else self.data)
            for bits in values[i-1] if i > 0 else self.data:
                if int(bits[i]) == deciding:
                    values[i].append(bits)

        return int(values[self.data_len-1][0], 2)

    def co2_scrubber(self):
        values = [[] for i in range(self.data_len)]
        for i in range(self.data_len):
            if len(values[i-1]) == 1:
                return int(values[i-1][0], 2)
            deciding = self.least_common(i, values[i-1] if i > 0 else self.data)
            for bits in values[i-1] if i > 0 else self.data:
                if int(bits[i]) == deciding:
                    values[i].append(bits)

        return int(values[self.data_len-1][0], 2)
        

    def part2(self):
        return self.oxygen_generator() * self.co2_scrubber()


        
if __name__ == "__main__":
    DATA_INPUT_LOCATION = "data.in"

    day = Day(DATA_INPUT_LOCATION)
    print(day.part1())
    print(day.part2())
