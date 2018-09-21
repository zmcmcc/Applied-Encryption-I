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

def decrypt_file():
    
    #generate upper and lower case alphabet
    caps,lower = gen_alphabet()
    
    #open input file
    message = open('input.txt','r')
    line = ''
    for newline in message.readlines():
        line = line + str(newline)
        
    message.close()
    print("The encrypted message is: ",line)
    
    #turn string from input into a list of characters
    letters = list(line)

    #in this loop, try every key from 1-25
    for key in range(1,25):
        text = []

        #decrypt every letter with the key
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
            
        # After decrypting all of the letters,
        # join the list text into a single string
        newMessage = ''.join(text)

        # Detect if the decrypted message is valid English
        # If so, write it in the output.txt file
        if detectEnglish(newMessage) == True:
            output = open('output.txt','w')
            output.write(newMessage)
            output.close()
            print ("The decrypted message is: ", newMessage)
            print ("The decrypted message is stored in output.txt")


#Call the function
decrypt_file()   
