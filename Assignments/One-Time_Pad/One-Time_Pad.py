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
    count_total = len(message_words)
    count = 0;
    for word in message_words:
        if word in words:
            count += 1
    percent = count/count_total

    #if the ratio is higher than 0.5, return true
    return percent > 0.5

def onetimePad():
    #generate upper and lower case alphabet
    caps,lower = gen_alphabet()
    
    #open the file and read the key and the plaintext
    file = open('input.txt','r')
    keys = file.readline()
    key_list = keys.split()
    plaintext = file.readline()
    letters = list(plaintext)
    file.close()

    #if the plaintext is English, do the one-time pad encryption
    if detectEnglish(plaintext):
        for i in range(len(plaintext)):
            text = []
            for letter in letters:
                
                #identify whether the letter is lower or upper-case
                if letter in lower:
                    num = lower.index(letter)
                    num = num + int(key_list[i]) # use the ith key
                    num = num % 26
                    letter = lower[num]
                elif letter in caps:
                    num = caps.index(letter)
                    num = num + int(key_list[i]) # use the ith key
                    num = num % 26
                    letter = caps[num]
                
                #append the shifted letter or the ignored symbol to the text list
                text.append(letter)
            
        # After decrypting all of the letters,
        # join the list text into a single string
        newMessage = ''.join(text)
        
        #Write it to a new file.
        newfile = open('encryption.txt','w')
        newfile.write(newMessage)
        newfile.close()
        
    elif not detectEnglish(plaintext):
        for i in range(len(plaintext)):
            text = []
            for letter in letters:
                
                #identify whether the letter is lower or upper-case
                if letter in lower:
                    num = lower.index(letter)
                    num = num + 26 - int(key_list[i]) # use the reverse of the ith key
                    num = num % 26
                    letter = lower[num]
                elif letter in caps:
                    num = caps.index(letter)
                    num = num + 26 - int(key_list[i]) # use the reverse of the ith key
                    num = num % 26
                    letter = caps[num]
                
                #append the shifted letter or the ignored symbol to the text list
                text.append(letter)
            
            newMessage = ''.join(text)
            
            #if the decryption is English, write it to a new file
            if detectEnglish(newMessage):
                output = open('decryption.txt','w')
                output.write(newMessage)
                output.close()
        

#Call the main function
onetimePad()
