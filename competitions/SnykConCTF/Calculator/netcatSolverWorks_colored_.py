from colorama import Fore, Back, Style

from sympy import *
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("35.211.207.36", 8000))
time.sleep(2)
data = s.recv(1024)
stringSocket = data.decode('utf-8') 
print(Fore.RED + stringSocket + Style.RESET_ALL)
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
    hackerString = "\nHACKING: " + str(i) + "% DONE!"
    s.send(str.encode(numString))
    print(Fore.GREEN + numString + hackerString + Style.RESET_ALL)
    time.sleep(7.3)
    newData = s.recv(1024)
    stringSocket = newData.decode('utf-8') 
    if i == 99:
        stringHacked = "HACKING COMPLETE PASSWORD == "
        print(Fore.GREEN + stringHacked + stringSocket + Style.RESET_ALL)
        exit()
    else:
        print(Fore.RED + stringSocket + Style.RESET_ALL)
    stringIndex = 1

