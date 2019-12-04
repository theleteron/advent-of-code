fromR = 272091
toR = 815432

def check_password(password):
    lowestValue = 0
    doubles = {}
    for char in password:
        if int(char) < lowestValue:
            return 0
        elif int(char) > lowestValue:
            lowestValue = int(char)
        elif int(char) == lowestValue:
            if not int(char) in doubles.keys():
                doubles[int(char)] = 1
            else:
                doubles[int(char)] += 1
        else:
            print("err")
            
    if 1 in doubles.values():
        print(password)
        return 1
    return 0

def gen_passwords(fromRange, toRange):
    valid = 0
    for password in range(fromRange, toRange+1):
        valid += check_password(str(password))
    return valid

print(check_password("112233"))
print(check_password("123444"))
print(check_password("111122"))
print(gen_passwords(fromR, toR))
