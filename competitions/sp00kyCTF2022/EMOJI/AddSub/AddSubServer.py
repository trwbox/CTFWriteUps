import socket
import threading
import sys
import random
import time

# Careful this runs on all addresses, while it shouldn't be a problem, be warned
globalAddress = '0.0.0.0'
globalPort = 8082
TIMEOUT = 60
CORRECTCOUNT = 10
FLAG = 'sp00ky{w3lc0m3_t0_3m0j1_m4th}'

# Emoji lookup table
EMOJILOOKUP = {
    0: '🔥',
    1: '🐍',
    2: '👻',
    3: '😱',
    4: '🎃',
    5: '😈',
    6: '👽',
    7: '💀',
    8: '🍖',
    9: '🍬',
} 

def runner(conn):
    try:
        # Start a timer for the connection
        startTime = time.time()
        # Keep track of how many problems they've solved
        correctCounter = 0
        while True:
            # If they've taken too long, close the connection
            if time.time() - startTime > TIMEOUT:
                conn.send(b'You took too long to complete the number of required problems\n')
                conn.send(b'Closing connection\n')
                conn.shutdown(socket.SHUT_RDWR)
                conn.close()
                return
            # Generate two random numbers
            int1 = random.randint(0, 999)
            int2 = random.randint(0, 999)
            # Select a random operation
            mathint = random.randint(0, 1)
            solution = None
            mathOP = None
            # Figure out the solution and the math operation
            if mathint == 0:
                solution = int1 + int2
                mathOp = '+'
                print(f'{int1} + {int2} = {solution}')
            elif mathint == 1:
                solution = int1 - int2
                mathOp = '-'
                print(f'{int1} - {int2} = {solution}')
           
            # Convert the ints to emoji with the lookup table
            int1str = ''
            int2str = ''
            for i in str(int1):
                int1str = int1str + EMOJILOOKUP[int(i)]
            for i in str(int2):
                int2str = int2str + EMOJILOOKUP[int(i)]
            
            # Log the ints and the solution
            print(f'Int1: {int1}:{int1str} Int2: {int2}:{int2str} OP: {mathOp} Solution: {solution}')
            # Send the problem to the client with the emojis and the math operation
            conn.send(f'What is {int1str} {mathOp} {int2str} = \n'.encode('utf-8'))
            
            # Receive the data from the client
            # It should be decoded as an integer
            data = conn.recv(1024)
            try:
                data = int(data.decode('utf-8'))
            # If it's not an integer, send an error message
            except ValueError:
                conn.send(b'Invalid input\n')
                conn.send(b'Closing connection\n')
                conn.shutdown(socket.SHUT_RDWR)
                conn.close()
                return
            # If the solution is correct, send a message and increment the counter, then repeat loop
            if data == solution:
                conn.send('Correct\n'.encode('utf-8'))
                correctCounter = correctCounter + 1
            # If the solution is incorrect, send a message with the correct answer and close the connection
            else:
                conn.send(f'Incorrect\nThe correct answer was {solution}\n'.encode('utf-8'))
                conn.send(b'Closing connection\n')
                break
            # If they've solved enough problems, send the flag and close the connection
            if correctCounter == CORRECTCOUNT:
                conn.send(f'You got {CORRECTCOUNT} correct in time\n'.encode('utf-8'))
                conn.send(b'Here is your flag:\n')
                conn.send(f'{FLAG}\n'.encode('utf-8'))
                conn.send(b'Closing connection\n')
                break
        
        conn.shutdown(socket.SHUT_RDWR)
        conn.close()
    # Except IOErrors and close the connection if the user disconnects
    except IOError as e:
        if e.errno == 32:
            print('Connection closed by client')
        else:
            # Other error
            print('Unknown Error')
            print(e)



def main():
    # This is the main method
    # Create a tcp socket that spawns a new thread on each connection
    address = globalAddress
    port = globalPort

    # Let the user specify the host if they want
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-p':
            port = int(sys.argv[i+1])
        if sys.argv[i] == '--port':
            port = int(sys.argv[i+1])
        if sys.argv[i] == '-a':
            address = sys.argv[i+1]
        if sys.argv[i] == '--address':
            address = sys.argv[i+1]
        if sys.argv[i] == '-h':
            print('Usage: python3 socketRecv.py -p <port> -a <address>')
            print('Default port is 8082 and host 0.0.0.0')
            exit()

    # Create the new socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Attempt to bind to the address
    try:
        sock.bind((address, port))
    except socket.error as e:
        print(e)
        print(f'Failed to bind to {address}:{port}')
        sys.exit(1)
    print('Socket loaded successfully listening for connection on port ' + str(port))
    print('Listening on ' + address)
    # Listening for up to 15 connections at a time
    sock.listen(15)
    # When a connection is made, spawn a new thread to handle it
    while True:
        try:
            conn, addr = sock.accept()
            print('New connection from ' + addr[0] + ':' + str(addr[1]))
            print('Starting new thread')
            threading.Thread(target=runner, args=(conn,)).start()
        except KeyboardInterrupt:
            break

    # On keyboard interrupt, close the socket
    print('Closing socket')
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

if __name__ == '__main__':
    main()
