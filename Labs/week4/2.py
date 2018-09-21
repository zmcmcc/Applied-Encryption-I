# This script will demonstrate the basics of manipulating a pre-existing message

#define our function
def gen_alphabet():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    caps = list(alphabet)
    lowers = list(alphabet.lower())
    return (caps,lowers)
  
    

#define our primary function
def StringCleaner(message):
    caps,lowers = gen_alphabet()
    
    #make every letter lower case for convenience
    message = message.lower()
    
    #make a list of all characters in message
    message_list =list(message)
    #if the first letter is not cap, we will turn it to cap.
    if message_list[0] in lowers:
        first_letter = lowers.index(message_list[0] )
        message_list[0] = caps[first_letter]
    
    while message_list[-1] == '':
        del message_list[-1]
        
    punctuation = ['.','?','!']
    if message_list[-1] not in punctuation:
        message_list.append('.')
        
    new_message = ''.join(message_list)
    print(new_message)
    
#call function
message = "We ArE TesTing WITh ThiS mESSAGe"
StringCleaner(message)