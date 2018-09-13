#A script for practice
def test():
    year = int(input('Please enter the year when you were born: '))
    
    booklist1 = ['a','b','c']
    booklist2 = ['o','p','q']
    booklist3 = ['x','y','z']
    
    if year <= 100 and year >=18:
        year = year + 1900
    elif year < 18:
        year = year + 2000


        
        
    age = 2018 - year
    if age <= 18:
        print ("Here's the our recommended book list for your age: ", booklist1)
    elif age > 18 and age <= 50:
        print ("Here's the our recommended book list for your age: ", booklist2)
    elif age > 50:
        print ("Here's the our recommended book list for your age: ", booklist3)
    else:
        print ("Sorry it\'s invalid input. Bye.")

#Run the function
test()
