def fastPower(g,A,N):
    a = g
    b = 1
    while A > 0:
        if A%2 == 1:
            b = (b*a)%N
        a = (a*a)%N
        A = A//2
    return b

def int2bin(integer):
    if integer == 0:
        return '00000000'
    binString = ''
    while integer:#integer>0
        if integer %2 == 1:
            binString = '1' + binString
        else:
            binString = '0' + binString
        integer //= 2

    while len(binString)%8 != 0:
        binString = '0' + binString
    return binString

def xorbit(binary,key):
    ciphertext = ''
    for i in range(len(binary)):
        ciphertext = ciphertext + str(int(binary[i])^int(key[i%len(key)]))
    return ciphertext

def bin2int(binary):
    return int(binary,2)

def bruteForceDH(g,p,A):
    for i in range(p):
        a = fastPower(g,i,p)
        if a == A:
            return i
    return 'unable to brute force'

binary = '0100110101011010'
key = int2bin(44867)

ciphertext = xorbit(binary,key)

plaintext = xorbit(ciphertext,key)
print(plaintext)
