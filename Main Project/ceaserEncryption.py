import string

def encrypt(_key, _userinput):
    def key(a):
        value = a

        while value > 25:
            print("SKRIV VALID NUMMER")
            exit()
        while value < 1:
            print("SKRIV VALID NUMMER")
            exit()
        return value

    text = _userinput
    shift = int(_key)
    _shift = int(key(shift))

    _shift %= 26
    print(f'Your key is {_shift}')

    alphabet = string.ascii_lowercase
    shifted = alphabet[_shift:] + alphabet[:_shift]
    table = str.maketrans(alphabet, shifted) # Translation, lksm alfabet start 1 blir shift start 1


    encrypted = text.translate(table) # Dette legger det inn

    print(encrypted)

def decrypt(_key, _userinput):
    def key(a):
        value = a

        while value > 25:
            print("SKRIV VALID NUMMER")
            exit()
        while value < 1:
            print("SKRIV VALID NUMMER")
            exit()
        return value

    text = _userinput
    shift = int(_key)
    _shift = int(key(shift))

    _shift %= 26
    print(f'Your key is {_shift}')

    alphabet = string.ascii_lowercase
    shifted = alphabet[_shift:] + alphabet[:_shift]
    table = str.maketrans(shifted, alphabet) # Translation, lksm alfabet start 1 blir shift start 1


    decrypted = text.translate(table) # Dette legger det inn

    print(decrypted)