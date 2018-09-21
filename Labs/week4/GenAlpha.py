# This script will demonstrate the basics of manipulating a pre-existing message

#define our function
def gen_alphabet():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    caps = list(alphabet)
    lowers = list(alphabet.lower())
    return (caps,lowers)