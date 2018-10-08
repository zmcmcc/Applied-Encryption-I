#This script determines if an input file is binary or not
#If the input file is binary, read and return alphabetic letters
#If not, then take the alphabetic letters and convert them to binary


# this function create the list of all the letters of the alphabet.
def gen_alphabet():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    caps = list(alphabet)
    lowers = list(alphabet.lower())
    
    return (caps,lowers)

#This function detect whether the input is binary.
def detectBinary(message):
    #message_words = message.split()
    for i in range(len(message)):
        if not message[i] in ['0','1',' ','\n']:
            return False
    return True


def BinaryRW():
    #generate upper and lower case alphabet
    caps,lower = gen_alphabet()
    
    #open the file and read the key and the plaintext
    file = open('input.txt','r')
    content = file.readline()
    #letters = content.split()
    file.close()

    
    text = []

    #Binary to words
    if detectBinary(content):

        #Get every byte
        bins = content.split(' ')

        for binary in bins:
            if binary == '00100000':#space
                text.append(' ')
            else:#get the corresponding letter
                order = int(binary[3:],2)#binary to decimal
                if binary[2]=='1':
                    text.append(lower[order-1])
                elif binary[2]=='0':
                    text.append(caps[order-1])

        resText = ''.join(text)
        
        return resText


    #Words to binary
    else:
        for letter in content:
            if letter == ' ':
                text.append('00100000')#space
                
            else:
                
                if letter in lower:
                    order = lower.index(letter) + 1
                    order_binary = bin(order)[2:]#decimal to binary

                    #fill in '0's if the binary has less than 5 digits
                    num_zeros = 5 - len(bin(order)[2:])
                    for i in range(num_zeros):
                        order_binary = '0'+order_binary
                    order_binary = '011'+ order_binary
                    text.append(order_binary)
                    
                elif letter in caps:
                    order = caps.index(letter) + 1
                    order_binary = bin(order)[2:]#decimal to binary

                    #fill in '0's if the binary has less than 5 digits
                    num_zeros = 5 - len(bin(order)[2:])
                    for i in range(num_zeros):
                        order_binary = '0'+order_binary
                    order_binary = '010'+ order_binary
                    text.append(order_binary)
                
                    
        resText = ' '.join(text)
        
        return resText
        

    


print(BinaryRW())


