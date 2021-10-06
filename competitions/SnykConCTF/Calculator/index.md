You need to put in a bunch of calculations to get the flag

Started off with a single equatiosn and how to solve it automatically with sympy, figured that out then moved onto making it interact with more than 1
Mainly by sending netcat to a file, reading the file in the program and printing the answer then manually putting in the answer for the problem and going to the next one. After hoping I could keep on with that, but couldn't figure it out I decided to dig into the basics of sockets since I had never touched them before.

Knew nothing very liitle sockets beforehand so it was all real new
Grabbed the data from the socket and got it into a string
Parsed the string into things that symnpy liked
used sympy to solve
converted to bytes to send to the socket
got the new data from the socket and parsed it into sympy compatible strings
set to repeat 500 times
Let it run til it crashed as the flag most likely would not be able to be parsed into an equation

//Solved


Pictures in my picture folder Need to complete the writing