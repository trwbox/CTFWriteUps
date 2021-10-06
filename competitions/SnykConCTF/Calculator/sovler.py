from sympy import *


f = open("/home/trwbox/Desktop/CTF Writeups/Work in Progress/SnykCon CTF/Calculator/equation.txt")
randomVal = true
stringEquation = ''
while randomVal:
    tempChar = f.read(1)
    if tempChar == '=':
        randomVal = false
    elif tempChar == '\n':
        randomVal = false
    else: 
        stringEquation = stringEquation + tempChar

randomVal = true
stringEquation2 = ''
while randomVal:
    tempChar = f.read(1)
    if tempChar == '=':
        randomVal = false
    elif tempChar == '\n':
        randomVal = false
    else: 
        stringEquation2 = stringEquation2 + tempChar




eq1 = parse_expr(stringEquation)
eq2 = parse_expr(stringEquation2)
equation = Eq(eq1, eq2)


sol = solve(equation)
print(sol)

