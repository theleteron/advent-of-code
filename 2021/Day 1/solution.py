def part1():
    data = open("data.in", "r")

    data_in = []
    increased   = 0

    for line in data:
        data_in.append(int(line))

    for i in range(len(data_in) - 1):
        if data_in[i] < data_in[i+1]:
            increased += 1
    
    return increased

def part2():
    data = open("data.in", "r")

    data_in = []
    windows = []
    increased   = 0

    for line in data:
        data_in.append(int(line))
        
    for i in range(len(data_in)-3 + 1):
        windows.append(sum(data_in[i:i+3]))

    for i in range(len(windows)-1):
        if windows[i] < windows[i+1]:
            increased += 1

    return increased

if __name__ == "__main__":
    print(part1())
    print(part2())