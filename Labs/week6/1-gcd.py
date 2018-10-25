
def gcd(a,b):
    if a < b:
        storage = a
        a = b
        b = storage
    res = 1
    while res != 0:
        res = a%b
        a = b
        b = res
    
    return a

def is_coprime(a,b):
    if gcd(a,b) == 1:
        return True
    else:
        return False
    
print(is_coprime(147,22))

a = 1
b=0

count = 1
        
while b !=1:
    a = a*42
    b = a%131
    count += 1
    
print(a)
print(count)
    
    
    
    