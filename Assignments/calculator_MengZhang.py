#   Made by Meng Zhang on September 6, 2018.
#   This scrpipt asks the user to enter one number and one kind of calculation
#(addition, multiplication, substraction and division), then input another number
#and let the script do the calculation.
#   This calculator support memory function.
#   The user can choose either to keep calculating with previous result,
#or start a new calculation.

#For the program to exit after use.
import sys

#   This function is for first-time calculation, to input the first number.
def calculator():
    num1 = float(input("Please input your first number for calculation: "))
    calculator2(num1)

#   This function is for continuing calculation.
def calculator2(num1):
    calculation = input("Please enter one of these four calculations:\n addition, substraction, multiplication and division. \nPlease use signals '+','-,''*','/' to represent them.")
    #Invalid input detection
    if not (calculation == '+' or calculation == '-' or calculation == '*' or calculation == '/'):
        print ('Invalid input. The program will shut down. Goodbye.')
        sys.exit()
        
    #input the second number
    num2 = float(input("Please input your second number for calculation: "))
    
    #Do the math according to the choice above, and print the result
    if calculation == '+':
        result = num1 + num2
        print('The result of your calculation of ',num1,' + ',num2,'is:  ',result)
    elif calculation == '/':
        result = num1 / num2
        print('The result of your calculation of ',num1,' / ',num2,'is:  ',result)
    elif calculation == '-':
        result = num1 - num2
        print('The result of your calculation of ',num1,' - ',num2,'is:  ',result)
    elif calculation == '*':
        result = num1 * num2
        print('The result of your calculation of ',num1,' * ',num2,'is:  ',result)

    #Let the user choose whether to continue calculating(with previous result, or start a new calculation), or exit.
    keepGoing = input("Please input '1' for continuing calculation, '2' to start a new calculation, or any other keys to exit the program. ")
    if keepGoing == '1':
        #Pass the result as the first number of the next calculation
        calculator2(result)
    elif keepGoing == '2':
        #Start from the first step agian
        calculator()
    else:
        print ('Thanks for using my calculator. Goodbye.')
        sys.exit()
    
#Call this function to strat the program.
calculator()

        
