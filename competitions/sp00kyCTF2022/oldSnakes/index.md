# oldSnakes

## Note this is a broken challenge, it does not work reliably, as many different operating systems all create teh sys.version string differently.

## Description

There is this old file that runs on our server, and it just works, but it fails every time I run it. Can you figure it out?

edit: It appears different version of python breaks thing.
My sys.version.encode() gives the byte string.
`b'3.8.10 (default, Jun 22 2022, 20:18:18) [GCC 9.4.0]'`
If you can describe to Trent, what you need to do to get a correct string, you will get handed the flag.

## Other information

Value: 125 points

Included files: [oldSnakes](oldSnakes)

### File contents

```py
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8081))
string = None
try:
    string = sys.version.encode()
except:
    string = sys.version
sock.send(string)
data = sock.recv(1024)
print(data)
```

## Solution

This challenge was meant to be solved, by running this program on a current version of python then receiving information back about your current version of python, compared to the version it was looking for.

Running this from my current WSL environment with the built in python, I get the following output:

```txt
b'That snakes major version is too old\nClosing connection'
```

Taking a look at the code there is a string being sent to the remote server that is being validated. With there being 2 different ways that this string gets created, the first is using the `sys.version.encode()` function, which will return a byte string. The second is using the `sys.version` function if that fails, which will return a string. While the socket will always send the same variable. This was a clue, that you needed the .encode() function to fail when running this program.

This can be used to help determine what version of python the server is looking for, as one of the major breaking changes between python 2 and python 3 was the change from strings to byte strings as a requirement for socket. However, python 2 is still too new of a version to be used for this challenge. While python 2 allows for strings or byte strings to be sent from a socket, it still has an encode(). This means that the encode() function will not fail, and the server will not receive the correct string. Taking a look at one of the new changes in python2 is the addition of byte strings, and the ability to decode and encode raw bytes. This means that you need to go a step further back to Python 1.

The Python 1 releases can be found here [https://www.python.org/download/releases/](https://www.python.org/download/releases/). If you could a get a binary release working on your machine, it would still fail with the server giving the error, `Invalid snake birthing date`. Looking at sys.version it includes the compilation date for python with my python1.5 having `1.5 (#2, Oct 29 2022, 10:54:48)  [GCC 9.4.0]`. The server is looking for a version of python 1.5 or 1.6 compiled in October 2022.

That means you would need to compile python yourself for the challenge, luckily source files are easily available on the release page, with Python 1.6 compiling with no issues on GCC 9.4, and Python 1.5 having a minor error, where both python and current stdio have an identically named function. With the name only occurring 2-3 times in the python source, it was easy to change the name of the function to get it to compile.

Running the script with the newly compiled version of python 1.5, gives the flag:

```txt
sp00ky{c0mpil3dFr0mS0urc3}
```

## Extra

If you would like to play with this on your own the server side code is available here [oldSnakesSocket.py](oldSnakesSocket.py). This is a python3 script not a python1 script.