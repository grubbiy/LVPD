import string

def key(a):
    value = a
    '''
    while value > 26:
        value /= 10
    '''
    while value < 1:
        value += 10
    return value

text = input("Skriv: ")
shift = int(input("1-26"))
_shift = int(key(shift))
_shift %= 26

print(f'Idc your key is {_shift}')

alphabet = string.ascii_lowercase
shifted = alphabet[_shift:] + alphabet[:_shift]
table = str.maketrans(alphabet, shifted) # Translation, lksm alfabet start 1 blir shift start 1

encrypted = text.translate(table) # Dette legger det inn

print(encrypted)