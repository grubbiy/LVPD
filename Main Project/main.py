from ceaserEncryption import encrypt, decrypt
import time

failed = False

time.sleep(2)

while True:
    print("""
    ██╗░░██╗██████╗░██╗░░░██╗██████╗░████████╗███████╗██████╗░███████╗██████╗░
    ██║░██╔╝██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔══██╗
    █████═╝░██████╔╝░╚████╔╝░██████╔╝░░░██║░░░█████╗░░██████╔╝█████╗░░██████╔╝
    ██╔═██╗░██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██╔══╝░░██╔══██╗██╔══╝░░██╔══██╗
    ██║░╚██╗██║░░██║░░░██║░░░██║░░░░░░░░██║░░░███████╗██║░░██║███████╗██║░░██║
    ╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""")
    if failed == True:
        print("Skriv en av følgende:")

    print("Skriv krypter for å kryptere\nSkriv dekrypter for å dekryptere\nTrykk enter for å forlate\n")
    answer = input("Svar: ")

    if answer.lower() == "krypter":
        print("""\n\n\n\n\n\n\n\n\n\n
██╗░░██╗██████╗░██╗░░░██╗██████╗░████████╗███████╗██████╗░
██║░██╔╝██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
█████═╝░██████╔╝░╚████╔╝░██████╔╝░░░██║░░░█████╗░░██████╔╝
██╔═██╗░██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██╔══╝░░██╔══██╗
██║░╚██╗██║░░██║░░░██║░░░██║░░░░░░░░██║░░░███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝\n""")
        userin = input("Skriv det du vil kryptere\nSvar: ")
        keyin = int(input("Skriv tall fra 1-25\nSvar: "))

        print("""\n\n\n\n\n\n\n\n\n\n\n
██╗░░██╗██████╗░██╗░░░██╗██████╗░████████╗███████╗██████╗░████████╗
██║░██╔╝██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗╚══██╔══╝
█████═╝░██████╔╝░╚████╔╝░██████╔╝░░░██║░░░█████╗░░██████╔╝░░░██║░░░
██╔═██╗░██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██╔══╝░░██╔══██╗░░░██║░░░
██║░╚██╗██║░░██║░░░██║░░░██║░░░░░░░░██║░░░███████╗██║░░██║░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░""")
        encrypt(keyin, userin)
        input("Trykk enter for å gå ut...")
        print("\n\n\n\n")

    elif answer.lower() == "dekrypter":
        print("""\n\n\n\n\n\n\n\n\n\n
██████╗░███████╗██╗░░██╗██████╗░██╗░░░██╗██████╗░████████╗███████╗██████╗░
██╔══██╗██╔════╝██║░██╔╝██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║░░██║█████╗░░█████═╝░██████╔╝░╚████╔╝░██████╔╝░░░██║░░░█████╗░░██████╔╝
██║░░██║██╔══╝░░██╔═██╗░██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██╔══╝░░██╔══██╗
██████╔╝███████╗██║░╚██╗██║░░██║░░░██║░░░██║░░░░░░░░██║░░░███████╗██║░░██║
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝\n""")
        userin = input("SKriv det du vil dekryptere\nSvar: ")
        keyin = int(input("SKriv tall fra 1-25\nSvar: "))

        print("""\n\n\n\n\n\n\n\n\n\n\n 
██████╗░███████╗██╗░░██╗██████╗░██╗░░░██╗██████╗░████████╗███████╗██████╗░████████╗
██╔══██╗██╔════╝██║░██╔╝██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗╚══██╔══╝
██║░░██║█████╗░░█████═╝░██████╔╝░╚████╔╝░██████╔╝░░░██║░░░█████╗░░██████╔╝░░░██║░░░
██║░░██║██╔══╝░░██╔═██╗░██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██╔══╝░░██╔══██╗░░░██║░░░
██████╔╝███████╗██║░╚██╗██║░░██║░░░██║░░░██║░░░░░░░░██║░░░███████╗██║░░██║░░░██║░░░
╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░""")
        decrypt(keyin, userin)
        input("Trykk enter for å gå ut...")
        print("\n\n\n\n")
    elif answer.lower() == "":
        print("""\n\n\n\n\n\n\n\n\n\n
░██████╗░░█████╗░░█████╗░██████╗░██████╗░██╗░░░██╗███████╗
██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝
██║░░██╗░██║░░██║██║░░██║██║░░██║██████╦╝░╚████╔╝░█████╗░░
██║░░╚██╗██║░░██║██║░░██║██║░░██║██╔══██╗░░╚██╔╝░░██╔══╝░░
╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██████╦╝░░░██║░░░███████╗
░╚═════╝░░╚════╝░░╚════╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝\n""")
        time.sleep(2)
        
        exit()
    else:
        print("\n\n\nInvalid input\n\n")
        time.sleep(1)
        print("Prøv igjen")
        time.sleep(1)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        failed = True