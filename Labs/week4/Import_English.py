#########
#This script requires a dictionary.txt file be in the same dir
#########



#This script will serve as a keeper of useful functions to be used inn
# your caesar cipher decryption script

#Specifically, these functions help you to get a head-start on a function that
#detects english for the sake of knowing when you have decrypted a message

def load():
    dictionary = open('dictionary.txt','r')
    words = []
    for word in dictionary.read().split('\n'):
        words.append(word)
        
    dictionary.close()
    
    return words


#remove non-letter symbols from message for the sake of checking for English
    
def noSpecials(message):
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


def detectEnglish(message):
    words = load()
    message = message.upper()
    message = noSpecials(message)
    message_words = message.split()
    count_total = len(message_words)
    count = 0;
    for word in message_words:
        if word in words:
            count += 1
    percent = count/count_total
    return percent > 0.8


message = 'This message is several words long. \
    Let\'s see how this handles punctuation.'
print(detectEnglish(message))
    
            
        
            
       
    