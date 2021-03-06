# This script will find a number's prime factors


#so as to avoid too much wasted computational time
# we will create a flag number
# because 1 is not prime and because 2 is the only even prime,
# we will start with 3
flag = 3

#our function will take 2 variables
#N: the number we are checking for primeness
# a: our flag

def is_prime(N,a):
    #we will use an if statement to check N against 'a'
    if N == 2 or N ==3:
        # print(N, ' is prime')
        prime = True
    elif N <= 1: # make sure the number being checked is appropriate
        prime = False
    elif N % 2 == 0:
        prime = False
    elif N % a == 0: #check if the number is divisible by the flag
        prime = False
    elif a ** 2 > N: #check if a^2 has not gone past N
        prime = True
    else:
        prime = is_prime(N,a+2)
    return prime

def find_factors(n):
    primes = []
    factors = []
    flag = 3
    if is_prime(n,flag):
        factors.append(n)

    else:
        for i in range(2,n//2 + 1):
            if is_prime(i,flag):
                primes.append(i)
        while n > 1:
            for p in primes:
                if n % p == 0:
                    n = n//p
                    factors.append(p)
    factors.sort()
    return factors

def read_input():
    numbers = open('input.txt','r')
    lines = numbers.readlines()
    print(lines)
    numbers.close()

    primes, non_primes = [],[]

    for line in lines:
        line = int(line)
        if is_prime(line,flag):
            primes.append(line)
        else:
            non_primes.append(line)

    choice = input('Which list do you want to see, the primes or the composites? ')
    if choice == 'primes':
        return primes
    elif choice == 'composites':
        return non_primes
    

    
print('The list is: ',read_input())
    
