from sympy import *
#test.txt came from "nc 35.211.207.36 8000 > test.txt"
f = open("/home/trwbox/Desktop/CTF Writeups/Work in Progress/SnykCon CTF/Calculator/test.txt")
f.read(331)


for i in range(500):
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
    numString = str(sol[0])
    print(sol[0])
    string = f.read(5)

