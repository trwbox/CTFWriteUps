from colorama import Fore, Back, Style
from sympy import *
import socket
import time

# Creates and connects to the socket that is hosting the challenge
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("35.211.207.36", 8000))
# Wait 2 seconds because it was occasionally slow and this guarteed dat
time.sleep(2)
# Receive the data from the socket and then convert it to a string
data = s.recv(1024)
stringSocket = data.decode('utf-8') 
# Make the string red and print it out onto the screen
print(Fore.RED + stringSocket + Style.RESET_ALL)
# Skip to position 331 in the string since that was the fixed length at the beginning without an equation
stringIndex = 331

# Set an arbitrary high number to loop through
for i in range(500):
    # Initate a boolean for the while loop and a string to store the equation before the equal sign
    randomVal = true
    stringEquation = ''
    while randomVal:
        # Takes the character at the stringIndex and sees if it is an equals sign or a new line, if it isn't adds it to the string
        tempChar = stringSocket[stringIndex]
        stringIndex = stringIndex + 1
        if tempChar == '=':
            randomVal = false
        elif tempChar == '\n':
            randomVal = false
        else: 
            stringEquation = stringEquation + tempChar

    # Initate a boolean for the while loop and a string to store the equation after the equal sign
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
    
    # Use sympy to parse the strings before and after the equal signs into equations that sympy can use
    eq1 = parse_expr(stringEquation)
    eq2 = parse_expr(stringEquation2)

    # Create an equation that sets the part before the equals sign to the part after it
    equation = Eq(eq1, eq2)
    # Solve the equation and put the value for the variable into an array
    sol = solve(equation)
    # Convert the int to the string for easier printing and encoding
    numString = str(sol[0])
    # Sends the correct answer encoded back to the server
    s.send(str.encode(numString))
    # Create a string that gives the number of times the loop has iterated and pretend it's that percent done hacking
    hackerString = "\nHACKING: " + str(i) + "% DONE!"
    # Prints out the hacker sting and the correct answer in green
    print(Fore.GREEN + numString + hackerString + Style.RESET_ALL)
    #Sleep for second that grab some more data before going back to the top of the loop
    time.sleep(1)
    newData = s.recv(1024)
    stringSocket = newData.decode('utf-8') 

    # So it doesn't end in a crash as it did when it wasn't colored and I knew it took 100 iterations
    if i == 99:
        # So at 100 iterations that string from the socket is the flag, so print hacking complete and the flag
        stringHacked = "HACKING COMPLETE PASSWORD == "
        print(Fore.GREEN + stringHacked + stringSocket + Style.RESET_ALL)
        exit()
    else:
        # Otherwise print the new equation received in red
        print(Fore.RED + stringSocket + Style.RESET_ALL)
    stringIndex = 1

