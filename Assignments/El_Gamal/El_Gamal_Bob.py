#This script is the implementation of the Bob side of El Gamal

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

#Some digit conversion functions
def bin2msg(binary):
    return ''.join(chr(int(binary[i*8:i*8+8],2)) for i in range(len(binary)//8))

def msg2bin(message):
    return ''.join(['{0:08b}'.format(ord(i)) for i in message])

def bin2dec(binary):
    return int(binary,2)

def msg2dec(message):
    return bin2dec(msg2bin(message))

def El_Gamal_Bob():
    
    #read p,g,A and a from input.txt
    with open('input.txt') as text:
        p = int(text.readline())
        g = int(text.readline())
        A = int(text.readline())
        a = int(text.readline())
    print(fastPower(g,a,p))

    #convert message to decimal value
    message = 'THX'    
    m = msg2dec(message)
    #random k
    k = random.randint(1,99999)
    
    C1 = fastPower(g,k,p)
    C2 = m * fastPower(A,k,p) % p

    vars = [str(p),str(g),str(a),str(C1),str(C2)]
    
    with open('output.txt','w') as output:
        for var in vars:
            output.write(var)
            output.write('\n')

El_Gamal_Bob()
