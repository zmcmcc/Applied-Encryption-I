#this short script demosntrates splitting a string into a list of words.

def demo_split():
    message = 'This message is several words long. \
    Let\'s see how this handles punctuation.'
    
    words = message.split()
    
    print(words)

demo_split()