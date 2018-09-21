# this script wil generate a list of all letters in the alphabet

#define our function
def gen_alphabet():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    caps = list(alphabet)
    lowers = list(alphabet.lower())
    return (caps,lowers)
   
#call function
gen_alphabet()