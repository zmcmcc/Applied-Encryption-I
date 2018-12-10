#This script is the implementation of Diffie-Hellman.

#This function does the fast power calculation
def fastPower(g,A,N):
    a = g
    b = 1
    while A > 0:
        if A%2 == 1:
            b = (b*a)%N
        a = (a*a)%N
        A = A//2
    return b

# this function create the list of all the letters of the alphabet.
def gen_alphabet():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    caps = list(alphabet)
    lowers = list(alphabet.lower())
    
    return (caps,lowers)

# this function will load the dictionary
def load_dictionary():
    dictionary = open('dictionary.txt','r')
    words = []
    for word in dictionary.read().split('\n'):
        words.append(word)
        
    dictionary.close()
    
    return words

#this function will remove non-letter symbols from message for the sake of checking for English
def remove_non_letter(message):
    #establish a string containing all letters
    caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # \t = tab
    letters = caps + caps.lower() + ' \t\n'
    
    #make a list of individual characters from message
    letterOnly = []
    for symbol in message:
        if symbol in letters:
            letterOnly.append(symbol)
            
    return (''.join(letterOnly))


# this function detects whether the decrypted massage is English
def detectEnglish(message):
    words = load_dictionary()
    
    # Make every letter uppercase since the dictionary is uppercase
    message = message.upper()
    
    message = remove_non_letter(message)

    #calculate the ratio of English words/ total words
    message_words = message.split()
    count_total = len(message_words)+1 #Avoid division by zero
    count = 0;
    for word in message_words:
        if word in words:
            count += 1
    percent = count/count_total

    #if the ratio is higher than 0.5, return true
    return percent >= 0.5


#this function invert decimal value into binary
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

#this function transfer binaries to letters
def binary2letter(content):
    cap,lower = gen_alphabet()
    #Get every byte (per 8 bits)
    bins = [content[i:i+8] for i in range(0, len(content), 8)]
    
    text = []
    for binary in bins:
        if binary == '00100000':#space
            text.append(' ')
        elif binary == '00101110':#.
            text.append('.')
        elif binary == '00101100':#,
            text.append(',')
        elif binary == '00100001':#!
            text.append('!')
        elif binary == '00111111':#?
            text.append('?')

        #get the corresponding letter
        #First check if this is a letter
        elif (binary[:3] == '011' or binary[:3] == '010'):
              if int(binary[3:],2) <= 26:
                  order = int(binary[3:],2)#binary to decimal
                  if binary[2]=='1':
                      text.append(lower[order-1])
                  elif binary[2]=='0':
                      text.append(cap[order-1])
        else:
            text.append('*')#Append '*' if this byte is not a letter

    resText = ''.join(text)
    return resText

#This function will calculate the XOR
def xorbit(binary,key):
    ciphertext = ''
    
    for i in range(len(binary)):
        ciphertext = ciphertext + str(int(binary[i])^int(key[i%len(key)]))
        
    return ciphertext

#this function removes '\n' if any to avoid error in xor.
def remove_linebreak(message):
    
    nums = '01'
    numsOnly = []
    for symbol in message:
        if symbol in nums:
            numsOnly.append(symbol)
            
    return (''.join(numsOnly))


#The main function to implement the Diffie Hellman
def diffie_hellman():
    
    #generate upper and lower case alphabet
    cap,lower = gen_alphabet()
    
    #read p,g,b,A and the binary text from input.txt
    with open('DHInput.txt') as text:
        p = int(text.readline())
        g = int(text.readline())
        b = int(text.readline())
        A = int(text.readline())
        txt = remove_linebreak(text.readline())
    #calculate the key
    key = fastPower(A,b,p)
    #convert it to binary
    key_binary = remove_linebreak(int2bin(key))

    txt = xorbit(txt,key_binary)

    txt_word = binary2letter(txt)

    #if it's English, then show it.
    if detectEnglish(txt_word):
        print("The message you have decrypted is: ",txt_word)
    #Otherwise, just show the encrypted binary text
    else:
        print("The message has been encrypted: ",txt)
        
        
diffie_hellman()
print(fastPower(22623,23367,23369))
