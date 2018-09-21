###
#GenAlpha.py and input.txt mush exist in the same dir
####

#This script will implement a Caesar Cipher

import GenAlpha

def encrypt_file():
    #generate upper and lower case alphabet via imported GenAlpha
    caps,lower = GenAlpha.gen_alphabet()
    
    #open input file
    message = open('input.txt','r')
    line = ''
    for newline in message.readlines():
        line = line + str(newline)
        
    message.close()
    
    #turn string from input into a list of characters
    letters = list(line)
    
    key = int(input('what key(1-25) would you like to use?'))
    
    text = []
    for letter in letters:
        #identify whether the letter is lower or upper-case
        if letter in lower:
            num = lower.index(letter)
            num = num + key
            num = num % 26
            letter = lower[num]
        elif letter in caps:
            num = caps.index(letter)
            num = num + key
            num = num % 26
            letter = caps[num]
        #append the shifted letter or the ignored symbol to the text list
        text.append(letter)
    #join the list text into a single string
    text = ''.join(text)
    print('The ciphertext is:\n' + text)
    
    output = open('output.txt','w')
    output.write(text)
    output.close()

encrypt_file()