import string

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def encrypt(_key, _userinput):
    def key(a):
        value = a

        while value > 25:
            print(colors.FAIL + "SKRIV VALID NUMMER")
            exit()
        while value < 1:
            print(colors.FAIL + "SKRIV VALID NUMMER")
            exit()
        return value

    text = _userinput
    shift = int(_key)
    _shift = int(key(shift))

    _shift %= 26
    print(colors.OKCYAN + f'Using key {_shift}')

    alphabet = string.ascii_lowercase
    shifted = alphabet[_shift:] + alphabet[:_shift]
    table = str.maketrans(alphabet, shifted) # Translation, lksm alfabet start 1 blir shift start 1


    encrypted = text.translate(table) # Dette legger det inn

    print(colors.OKCYAN + f"Encrypted: {encrypted}")

def decrypt(_key, _userinput):
    def key(a):
        value = a

        while value > 25:
            print(colors.FAIL + "SKRIV VALID NUMMER")
            exit()
        while value < 1:
            print(colors.FAIL + "SKRIV VALID NUMMER")
            exit()
        return value

    text = _userinput
    shift = int(_key)
    _shift = int(key(shift))

    _shift %= 26
    print(colors.OKCYAN + f'Using key {_shift}')

    alphabet = string.ascii_lowercase
    shifted = alphabet[_shift:] + alphabet[:_shift]
    table = str.maketrans(shifted, alphabet) # Translation, lksm alfabet start 1 blir shift start 1


    decrypted = text.translate(table) # Dette legger det inn

    print(colors.OKCYAN + f"Decryption: {decrypted}")