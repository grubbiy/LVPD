def key(a):
    value = a
    while value > 10:
        value /= 10
    while value < 1:
        value += 10
    return value

userKey = int(input("Your key will be a number from 1-10: "))

actualKey = int(key(userKey))

print(f'Your key will be {actualKey}')