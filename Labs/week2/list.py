#this script demonstrates the use of a list


#this function will create a list of books
#th user will then be asked if they would liek to add to the list
#at which point they will be given the option to do so

def make_list():
    #create the list and populate it with 3 books
    books = ['harry potter','hunger games','1984']
    print ('The original book list is: \n ',books)

    #prompt user to add to list
    addFav = input('\n Would you like to add a new book to the list? ')

    #write and if statement to deal with yes or no answers
    if addFav == 'no':
        print('in the list of favorite books remains unchanged.')
    elif addFav == 'yes':
        newBook = input('please enter the name of the book: ')
        books.append(newBook)

        print('\n the new list is: ',books)

        #in the event of a non yes nor no answer
        #explain the error and exit function
    else:
        print('\n I don\'t understand that response. Goodbye.')


    

#call it
make_list()
