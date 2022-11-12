# This is a combined solution for both math challenges.
import socket
import sys

# Create this lookup table by taking many wrong answers, and them
# figuring out what emoji is associated with what number.
EMOJILOOKUP = {
    '🔥': 0, 
    '🐍': 1,
    '👻': 2, 
    '😱': 3, 
    '🎃': 4, 
    '😈': 5, 
    '👽': 6, 
    '💀': 7, 
    '🍖': 8, 
    '🍬': 9
}

# Create a new socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
sock.connect(('localhost', 8083))
while True:
    # Read the data from the server
    data = sock.recv(1024)
    # If decode and slit the data
    split = data.decode('utf-8').split()
    # The math problems split in a 6 length list, so if it's not 6 make a different decision
    if len(split) != 6:
        # The correct answer line has 8 length so it can be ignored
        # Anything else is an a flag
        if len(data.decode('utf-8')) != 8:
            print("FLAG: " + data.decode('utf-8'))
            sys.exit(0)
        else:
            print('SOCKET SENT: ' + data.decode('utf-8'))
    # If the data is a problem
    elif len(split) == 6:
        # Get the first number by turning the emoji split back into a string
        int1 = ""
        for i in split[2]:
            int1 = int1 + str(EMOJILOOKUP[i])
        # Then convert that string back into a number
        int1 = int(int1)
        # Do the same for the second number
        int2 = ""
        for i in split[4]:
            int2 = int2 + str(EMOJILOOKUP[i])
        int2 = int(int2)
        # Create a variable to hold the solution
        sendingValue = 0
        # Check for the math operation, and do the math
        if split[3] == '+':
            sendingValue = int1 + int2
        elif split[3] == '-':
            sendingValue = int1 - int2
        elif split[3] == '*':
            sendingValue = int1 * int2
        elif split[3] == '//':
            sendingValue = int1 // int2
        elif split[3] == '%':
            sendingValue = int1 % int2
        # Send the solution back to the server
        sock.send(str(sendingValue).encode('utf-8'))