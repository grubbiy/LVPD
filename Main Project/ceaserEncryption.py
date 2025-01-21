
# Noge eg bare prøvde:
'''def ceaser(a):
    data = a.lower()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    newSentence = ""
    for i in range(a):
        for i in range(alphabet):
            times = i
            if a[times] == alphabet[i]:
                newSentence += alphabet[i]
    return newSentence

inndata = input("Skriv noko her: ")

result = ceaser(inndata)

print(result)
'''

import string

def key(a):
    value = a
    while value > 26:
        value /= 10
    while value < 1:
        value += 10
    return value

text = input("Skriv: ")
shift = int(input("1-26"))
_shift = int(key(shift))

print(f'Idc your key is {_shift}')

alphabet = string.ascii_lowercase
shifted = alphabet[_shift:] + alphabet[:_shift]
table = str.maketrans(alphabet, shifted) # Translation, lksm alfabet start 1 blir shift start 1

encrypted = text.translate(table) # Dette legger det inn

print(encrypted)