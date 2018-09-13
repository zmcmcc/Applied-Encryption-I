#This script demonstrates the use of for loops

#we are going to do this by looking at several methods by which to print half of
# the books in a list of books


#import the random functions
import random

#define our function
def make_list():
    #create a list of books
    books = ['a','b','c','d','e','f']

    #method 1: by index - first half of the list
    #this method will print elements at books[0],books[1],..until
    #the index i in books[i] is a half of the length of our list
    print('method 1')
    # // means 整除
    for i in range(len(books)//2):
        print(books[i])

    #method 2: only even index
    print('\nmethod 2')
    for i in range(len(books)):
        if i%2 == 0:
            print(books[i])

    #method 3: second half by way of counter
    print('\nmethod 3')
    c = 0 #counter
    for i in books:
        if c >= len(books)//2:
            print (i)
        c = c + 1

    #method 4: random selection
    print('\n method 4')
    #random.sample is afunction that takes 2 variables: a list and a number
    randomSet = random.sample(range(len(books)),len(books)//2)
    print(randomSet)
    for i in randomSet:
        print(books[i])


make_list()
