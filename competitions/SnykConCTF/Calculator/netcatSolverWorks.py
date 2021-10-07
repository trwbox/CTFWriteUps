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
# Print out the data received from the socket so you can see what is happening
print(stringSocket)
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
        # Takes the character at the stringIndex and sees if it is an equals sign or a new line, if it isn't adds it to the string
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
    # Prints the value sent to the server so you can see what is happening
    print(sol[0])
    # Wait a second to make sure the server had responded
    time.sleep(1)
    # Grab the new data and convert it into a string
    newData = s.recv(1024)
    stringSocket = newData.decode('utf-8') 
    # Print the string so you know what is going on
    print(stringSocket)
    # Sets the stringIndex back to one as the new data is only the new equation
    stringIndex = 1

