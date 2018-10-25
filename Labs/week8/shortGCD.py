#this code will run through the basic euclidean algorithm

def gcd(a,b):
    while b:
        a,b = b, a%b
    return a

print(gcd(27352,7688))
