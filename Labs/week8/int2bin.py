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

print(int2bin(25642))
