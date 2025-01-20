def writeBackwards(data):
    backwards = ""
    backwards += data[::-1]
    return backwards

datainput = input("Kva vil du skrive baklengs?: ")

result = writeBackwards(datainput)

print(result)