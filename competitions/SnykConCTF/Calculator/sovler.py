from sympy import *

#Using this to let the script work on anyone's machine
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "equation.txt")

# Have a file with a single equation to use as a test equation that I can parse and find the answer to
f = open(filename)

# Print out the file for easy comparison and seek to the beginning
string = f.read()
print(string)
f.seek(0, 0)

#Set a boolean value for while loop and a string for the values before the equals sign
randomVal = true
stringEquation = ''
while randomVal:
    # Take all the values before the equals sign and store it in a string
    tempChar = f.read(1)
    if tempChar == '=':
        randomVal = false
    elif tempChar == '\n':
        randomVal = false
    else: 
        stringEquation = stringEquation + tempChar

#Set a boolean value for while loop and a string for the values after the equals sign

randomVal = true
stringEquation2 = ''
while randomVal:
    # Take all the values after the equals sign and store it in a string
    tempChar = f.read(1)
    if tempChar == '=':
        randomVal = false
    elif tempChar == '\n':
        randomVal = false
    else: 
        stringEquation2 = stringEquation2 + tempChar

# Parse the string from each sid eof the equals sign into an expression that sympy can use
eq1 = parse_expr(stringEquation)
eq2 = parse_expr(stringEquation2)
# Set the 2 expressions equal to each other
equation = Eq(eq1, eq2)

# Use sympy to solve the equation and put into an array then print the answer
sol = solve(equation)
print(sol)

