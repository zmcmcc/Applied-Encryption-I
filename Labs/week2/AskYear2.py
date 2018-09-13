#this script demonstrate the use of an IF statement

#prompt the user to enter their birth year
# account for YY and YYYY formatting

def AskYear():
    year = input('Please enter your born year: ')
    year = int(year)
    #run on if statement to compensate for users who enter in YY format
    if year <= 100 and year >=18:
        year = year + 1900
    elif year < 18:
        year = year + 2000

    #run the calculation and print
    print('Your age is: ', 2018 - year, 'this year')

AskYear()
