#This script calculates the inverse of a number g modulo p, where p is prime.
    

def findInverse(g,p):
    #read the g and p from input.txt
    with open('input.txt') as text:
        p = int(text.readline())
        g = int(text.readline())
        
    t = p - 2 #t is p-2
    nums = []# to append g^2^n for n from 1 to some threshold number
    i = 1
    res = 1
    
    while(i <= t):
        nums.append((g**i)%p)
        i = i*2

    #turn p-2 into binary and inverse the order 
    t_bin = bin(t)[2:]
    t_bin_reverse = t_bin[::-1]
    
    #find the indice of the digits that the value sum to be p-2,
    #then multiply them mod p to get the result
    for digit in range(len(t_bin_reverse)):
        if t_bin_reverse[digit] == '1':
            res = res * nums[digit] % p

    print("The inverse number of {} modulo {} is: {}.".format(g,p,res))



findInverse(11,13)
