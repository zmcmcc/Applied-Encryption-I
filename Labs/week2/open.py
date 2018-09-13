#this script will demonstrate how to read an external text file
# usering read, readline and readlines

#define the function to read a .txt file

def example_open():
    # the first thing to do whenever readng an external file is to
    # open the file using the open function open('filename','mode')
    # mode can be 'r','w', or 'a' for append
    # append will add lines to the existing file

    #assign a variable to represent the open file
    #this allows you to identify which file you are reading from

    example = open('input.txt','r')

    #the reading function will return a string
    #consisting of a single line from the text file
    #successive uses of readline will read successive lines
    #line = example.readline()
    #print(line)
    #print('this is the first line of your readed txt file')

    #line = example.readline()
    #print(line)
    #print('this is the second line of your readed txt file')

    lines = example.readlines()
    print(lines)
    print('this is the entire content of your readed txt file')

    example.close()

    example = open('input.txt','r')
    whole = example.read()
    print(whole)
    print('this should print the entire txt file')
    #close your file
    example.close()

    


    
#call it
example_open()
