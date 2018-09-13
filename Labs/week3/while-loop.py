#this script demonstrates the use of while loops
#by calculating all prime factors of a number

def find_factors():

    #we will cheat a little by creating a list of low value prime numbers
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

    # establish the number to factor
    # for convenience we will use user input
    number = int(input('What number would you like to factor? '))

    #before we start factoring, let's make an empty list to record our factors
    factors = []

    #start the while loop to keep factoring as long as number is > 1
    while number > 1:
        for prime in primes:
            if number%prime == 0:
                number = number//prime
                factors.append(prime)
            #else:
                #factors.append(number)

    #sort our factor list in the event one factor appears several times
    factors.sort()


find_factors()
