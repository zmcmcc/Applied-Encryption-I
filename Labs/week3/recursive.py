# This script uses recursive function to determine if a number is a prime number

number = int(input('What number would you like to check for primeness? '))

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
        print(N, ' is prime')
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

print(is_prime(number,flag))
    
