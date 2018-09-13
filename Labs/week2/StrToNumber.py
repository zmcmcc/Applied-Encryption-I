# this script will demonstrate how to convert a string
# from user input into a number for performing calculations

#define a function that asks a user to input the year they were born
#run some math that returns the age.
def ageCalculation():
    year = input('Please input the year when you were born: ')
    year = int(year)
    age = 2018 - year
    print('Your age is: ',age)

ageCalculation()
