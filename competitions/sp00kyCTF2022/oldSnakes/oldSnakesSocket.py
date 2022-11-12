# This is highly broken on anything, but some Linux distros
# It would need a lot of work to be truly OS agnostic, while still 
# preventing the user from just sending the date
import socket
import threading
import sys

# Careful this runs on all addresses, while it shouldn't be a problem, be warned
globalAddress = '0.0.0.0'
globalPort = 8081
FLAG = 'sp00ky{c0mpil3dFr0mS0urc3}'
# The date of the challenge since we want the python to be compiled today
DATE = '29'


def runner(conn):
    data = conn.recv(1024)
    print(data)
    string = None
    # Try to decode the data into a sys.version string
    # Since the correct string is always ascii, anything else is wrong
    try:   
        string = data.decode('ascii')
    except UnicodeDecodeError:
        conn.send(b'Not ASCII\n')
        conn.shutdown(socket.SHUT_RDWR)
        conn.close()
        return
    # If the string is a sys.version string, split it into the sections to check the length
    string = string.split(' ')
    if len(string) not in [8, 9, 10]:
        conn.send(b'Invalid Length leaving\n')
        conn.shutdown(socket.SHUT_RDWR)
        conn.close()
        return

    # Split the version number into the sections
    number = string[0].split('.')
    print(number)
    # Check that the version number is 2 or 3 long
    if len(number) not in [2, 3]:
        conn.send(b'Invalid snake number\n')
        conn.shutdown(socket.SHUT_RDWR)
        conn.close()
        return
    
    # Check that the first number for being 1
    if int(number[0]) < 1:
        conn.send('That snakes major version is too young\n'.encode('utf-8'))
        conn.send('Closing connection'.encode('utf-8'))
        return
    elif int(number[0]) > 1:
        print('That snake is too old')
        conn.send('That snakes major version is too old\n'.encode('utf-8'))
        conn.send('Closing connection'.encode('utf-8'))
    elif int(number[0]) == 1:
        # Check that the minor number is 5 or 6
        if int(number[1]) < 5:
            conn.send('That snakes minor version is too young\n'.encode('utf-8'))
            conn.send('Closing connection'.encode('utf-8'))
            return
        elif int(number[1]) > 6:
            conn.send('That snake minor version is too old\n'.encode('utf-8'))
            conn.send('Closing connection'.encode('utf-8'))
            return
        elif int(number[1]) in [5, 6]:
            # Check that the data is the correct since we want it compiled today
            # This needs to be updated to the date of spooky
            if string[2] != 'Oct' or string[3] != DATE or string[4] not in ['2022', '2022,']:
                conn.send('Invalid snake birthing date\n'.encode('utf-8'))
            else:
                conn.send(f'{FLAG}'.encode('utf-8'))
    else: 
        conn.send('Broken value\n'.encode('utf-8'))
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()

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
            print('Default port is 8081 and host 0.0.0.0')
            exit()


    # Create the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Attempt to bind to the address
    try:
        sock.bind((address, port))
    except socket.error as e:
        print(e)
        print(f'Failed to bind to {address}:{port}')
        sys.exit(1)
    # Log that we are listening
    print('Socket loaded successfully listening for connection on port ' + str(port))
    print('Listening on ' + address)
    # Listen for connections up to 15 at a time
    sock.listen(15)
    # When a connection is made, spawn a new thread to handle it
    while True:
        try:
            conn, addr = sock.accept()
            threading.Thread(target=runner, args=(conn,)).start()
        except KeyboardInterrupt:
            break

    # On keyboard interrupt, close the socket
    print('Closing socket')
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

if __name__ == '__main__':
    main()
