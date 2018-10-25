#this script will determine whether or not a number generates a modulus p

def isGenerator(g,p):
    g = g % p
    checker = g
    generated = [g]
    while checker != 1:
        checker = checker * g % p
        generated.append(checker)
        if len(generated) > p:
            print('this number is not a generator')
            break

    #print(generated)
    if len(generated) == p - 1:
        return True
    else:
        return False


print(isGenerator(4,24))
