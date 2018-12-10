# This script is an emulator of the Enigma Machine used in WW2.
# The input plaintext must be lower case English letters from a-z, with NO space.
# This Enigma machine has 3 rotors.
# For each input letter, the first rotor will rotate by 1 letter.
# Once the first rotor finish a cycle(rotate 26 times), the second rotor will rotate by 1 letter.
# Once the second rotor finish a cycle(rotate 26 times), the third rotor will rotate by 1 letter.

import re #Regular Expressions

 
# This function judges if the input and the replace rotors are in valid format. 
def is_str(password, replace_word):
    an = re.match('[a-z]+$', password) #Use regular expression to judge if the input only contains lower case letters without space. 
    if not type(password) == type(replace_word) == type('a'):
        print('The input must be string!')
        return False
    elif not an:
        print('The input must only contain lower case letters!')
        return False
    elif len(replace_word) != 26:
        print('The replace word must be 26 letters long!')
        return False
    else:
        return True
 
 # This function rotate a rotor by one letter.
def rotors(replace_word):
    return replace_word[1:] + replace_word[0]
 
# This function reflect the letter after three rotors.
def reflector(word):# Use a dictionary to achieve the one-to-one reflection
    dic = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q',
           'e': 'r', 'f': 's', 'g': 't', 'h': 'u',
           'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y',
           'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
           'q': 'd', 'r': 'e', 's': 'f', 't': 'g',
           'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
           'y': 'l', 'z': 'm'}
    return dic[word]

#This is the main function.
def main(password, replace_word1, replace_word2, replace_word3):
    count = 0  # Counter of input letters
    new_pass = ''  # store the transferred message
    ori_table = 'abcdefghijklmnopqrstuvwxyz'  # The original table
    
    for obj in password:
        
        table1 = str.maketrans(ori_table, replace_word1)  # build the mapping of Rotor 1
        table2 = str.maketrans(ori_table, replace_word2)  # build the mapping of Rotor 2
        table3 = str.maketrans(ori_table, replace_word3)  # build the mapping of Rotor 3
        
        new_obj = str.translate(obj, table1)  # transfer the letter through Rotor 1
        new_obj = str.translate(new_obj, table2)  # transfer the letter through Rotor 2
        new_obj = str.translate(new_obj, table3)  # transfer the letter through Rotor 3
        
        new_obj = reflector(new_obj)  # get the reflected letter
        
        reverse_table1 = str.maketrans(replace_word1, ori_table)  # build the revresed mapping of Rotor 1
        reverse_table2 = str.maketrans(replace_word2, ori_table)  # build the revresed mapping of Rotor 2
        reverse_table3 = str.maketrans(replace_word3, ori_table)  # build the revresed mapping of Rotor 3
        
        new_obj = str.translate(new_obj, reverse_table3)  # transfer the letter through Rotor 3
        new_obj = str.translate(new_obj, reverse_table2)  # transfer the letter through Rotor 2
        new_obj = str.translate(new_obj, reverse_table1)  # transfer the letter through Rotor 1
        
        new_pass += new_obj  # Add the transfered letter to the list

        count += 1
        
        replace_word1 = rotors(replace_word1)  # rotate Rotor 1 by one letter for every input
        if count % 26 == 0:  # rotate Rotor 1 by one letter for every 26 inputs
            replace_word2 = rotors(replace_word2)
        elif count % 676 == 0:  # rotate Rotor 1 by one letter for every 26*26 input
            replace_word3 = rotors(replace_word3)
            
    return new_pass 


while True:
    #input
    a_password = input('Please input the message in lowercase with no space:')

    #set three rotors
    r_password1 = 'qwertyuiopasdfghjklzxcvbnm'
    r_password2 = 'qazwsxedcrfvtgbyhnujmikolp'
    r_password3 = 'qpwoalskeirutydjfhgzmxncbv'
    
    if is_str(a_password, r_password1) and is_str(a_password, r_password2) and is_str(a_password, r_password3):
        print('The transferred message is: ', main(a_password, r_password1, r_password2, r_password3))
        pass
