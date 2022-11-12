import socket
import sys

# Create a new socket and connect to the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8081))
string = None
# Try to encode the version string, but python1.5 does not have 
# that function, so if it fails, just use the string
# This will let this code run on python1.5 and python3 at the same time
try:
    # This ends up with a byte string python3 can send
    string = sys.version.encode()
except:
    # While this ends up with a string python1.5 can send
    string = sys.version

# Send then receive the data
sock.send(string)
data = sock.recv(1024)
print(data)
