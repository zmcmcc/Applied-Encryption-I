#This script is the implementation of the Alice side of El Gamal

import random

#This function does the fast power calculation
def fastPower(g,A,N):
    a = g
    b = 1
    while A > 0:
        if A%2 == 1:
            b = (b*a)%N
        a = (a*a)%N
        A = A//2
    return b


#Some digits conversion functions
def bin2msg(binary):
    return ''.join(chr(int(binary[i*8:i*8+8],2)) for i in range(len(binary)//8))


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


def El_Gamal_Alice():
    #read p,g,A and a from input.txt
    with open('output.txt') as text:
        p = int(text.readline())
        g = int(text.readline())
        a = int(text.readline())
        C1 = int(text.readline())
        C2 = int(text.readline())
    tmp = fastPower(C1,a,p)
    c1_to_a_inverse = fastPower(tmp,p-2,p)
    m = c1_to_a_inverse * C2 % p
    m_bin = int2bin(m)
    message = bin2msg(m_bin)
   
    print('The message from Bob is: ',message)

El_Gamal_Alice()
