def krypter(a):
    even = a[0::2]
    odd = a[1::2]
    kryptert = even + odd
    return kryptert
konfigurasjon = [3, 4, 5, 5, 3]
def bedreKrypt(b):
    dobbel = ""
    for i in range(len(b)):
        dobbel += b[i]+b[i]

    baklengs = b[::-1]

    bakOdd = baklengs[0::2]
    bakEven = baklengs[1::2]

    framOdd = b[0::2]
    framEven = b[1::2]

    '''
    ekstraSetup = len(b)//3 # Int versjon av deling
    ekstra1 = dobbel[0:ekstraSetup]
    ekstra2 = dobbel[ekstraSetup:(ekstraSetup * 2)]
    ekstra3 = dobbel[(ekstraSetup * 2):(ekstraSetup * 3)]
    '''


    resultat = bakOdd+framOdd+bakEven+framEven

    return resultat

inndata = input("Kva vil du kryptere?")

resultat = bedreKrypt(inndata)
print(f'Din kryptering er: {resultat}')
