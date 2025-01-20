def checkforCaps(data):
    capsAmount = 0
    for i in range(len(data)):
        if data[i].isupper():
            capsAmount += 1
    return capsAmount

datainput = input("Skriv noko med caps: ")
dataResult = checkforCaps(datainput)

print(f'Du har {dataResult} store bokstaver')