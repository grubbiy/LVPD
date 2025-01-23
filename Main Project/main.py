from ceaserEncryption import encrypt, decrypt
import time

while True:
    print("Skriv kryptere for å kryptere\nSkriv dekryptere for å dekryptere\nTrykk enter for å forlat\n")
    answer = input("Svar: ")

    if answer.lower() == "kryptere":
        userin = input("SKriv det du vil kryptere:\n\n")
        keyin = int(input("SKriv tall fra 1-25"))

        print(f"\n\nUsing")

        encrypt(keyin, userin)
        input("Trykk enter for å gå ut...")
        print("\n\n\n\n")

    elif answer.lower() == "dekryptere":
        userin = input("SKriv det du vil dekryptere:\n\n")
        keyin = int(input("SKriv tall fra 1-25"))

        decrypt(keyin, userin)
        input("Trykk enter for å gå ut...")
        print("\n\n\n\n")
    elif answer.lower() == "":
        print("\n\n\n\n\n\n\n\n\nTakk for bruken\n\n\n\n\n")
        time.sleep(2)
        exit()
    else:
        print("Skriv en av følgende:")