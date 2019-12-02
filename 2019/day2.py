#!/usr/bin/python3
goal = 19690720

def func(x, y):
    in_d2 = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,1,6,23,27,1,27,5,31,2,31,10,35,2,35,6,39,1,39,5,43,2,43,9,47,1,47,6,51,1,13,51,55,2,9,55,59,1,59,13,63,1,6,63,67,2,67,10,71,1,9,71,75,2,75,6,79,1,79,5,83,1,83,5,87,2,9,87,91,2,9,91,95,1,95,10,99,1,9,99,103,2,103,6,107,2,9,107,111,1,111,5,115,2,6,115,119,1,5,119,123,1,123,2,127,1,127,9,0,99,2,0,14,0"
    array = in_d2.split(',')
    resul = []
    lenArr = len(array)
    
    for i in range(lenArr):
        array[i] = int(array[i])
        resul.append(array[i])

    array[1] = x
    array[2] = y
    resul[1] = x
    resul[2] = y
    i = 0
    while True:
        if (array[i] == 99):
            if (resul[0] == goal):
                print("Found " + str(x) + " " + str(y) +
                      " and result " + str(100*x+y))
                return 0
            else:
                return 1
        if (array[i] == 1):
            resul[array[i+3]] = resul[array[i+1]] + resul[array[i+2]]
        elif (array[i] == 2):
            resul[resul[i+3]] = resul[array[i+1]] * resul[array[i+2]]
        else:
            return 1
        i += 4

for i in range(100):
    for j in range(100):
        if(func(i,j)==0):
            break
