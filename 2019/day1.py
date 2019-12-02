#!/usr/bin/python3
import math

fo = open("in_d1.txt", "r")
total = 0
res = 0

for line in fo:
    temp = line
    while True:
        if ((math.floor(int(temp)/3) - 2) > 0):
            res += math.floor(int(temp)/3) - 2
            temp = math.floor(int(temp)/3) - 2
        else:
            break
    total += math.floor(int(line)/3) - 2

print("Total fuel w/o fueal mass: " + str(total))
print("Total fuel w fueal mass: " + str(res))
