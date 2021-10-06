from sympy import *
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("35.211.207.36", 8000))
time.sleep(2)
data = s.recv(1024)
stringSocket = data.decode('utf-8') 
print(stringSocket)
stringIndex = 331

for i in range(500):
    randomVal = true
    stringEquation = ''
    while randomVal:
        tempChar = stringSocket[stringIndex]
        stringIndex = stringIndex + 1
        if tempChar == '=':
            randomVal = false
        elif tempChar == '\n':
            randomVal = false
        else: 
            stringEquation = stringEquation + tempChar

    randomVal = true
    stringEquation2 = ''
    while randomVal:
        tempChar = stringSocket[stringIndex]
        stringIndex = stringIndex + 1 
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
    s.send(str.encode(numString))
    print(sol[0])
    time.sleep(1)
    newData = s.recv(1024)
    stringSocket = newData.decode('utf-8') 
    print(stringSocket)
    stringIndex = 1

