import time

def key(a):
    value = a
    while value > 10:
        value /= 10
    while value < 1:
        value += 10
    return value

def writeBackwards(data):
    backwards = ""
    backwards += data[::-1]
    return backwards

def checkforCaps(data):
    capsAmount = 0
    for i in range(len(data)):
        if data[i].isupper():
            capsAmount += 1
    return capsAmount

userKey = int(input("Your key will be a number from 1-10: "))
actualKey = int(key(userKey))
time.sleep(1)

print(f'Your key will be {actualKey}')
time.sleep(2)
