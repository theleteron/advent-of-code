# Part 1 - Ugly code :D
elves = [0]
elf_id = 0
with open("data.in", "r") as file:
    for row in file:
        if row not in ['\n', '\r\n']:
            elves[elf_id] += int(row)
        else:
            elves.append(0)
            elf_id += 1

print(sorted(elves)[-1]+sorted(elves)[-2]+sorted(elves)[-3])
