def fastPower(g,A,N):
    a = g
    b = 1
    while A > 0:
        if A%2 == 1:
            b = (b*a)%N
        a = (a*a)%N
        A = A//2
    return b

print(fastPower(7,15,17))
