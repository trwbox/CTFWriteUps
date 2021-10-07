---
layout: writeup
title: Calculaor (SnykCon CTF 2021)
---
# Calculator

On the challenge you were given the command ```nc 35.211.207.36 8000``` and when running the command you are greeted with ```CALC-UL8R``` in ASCII art, and an equation with a line after with the variable and an equals sign. After putting in the right value it prints a new equation, and if you give the wrong solution it gives ```ERROR DOMAIN```.

So my first thought was that you need to solve a bunch of equations, and it will give you the flag. So the first thing I did was start trying to figure out a way to parse the equation and solve for the variable that was being asked for.

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

SNYK{37d779963c037715c02624b6963008f55e92d12e8714a15b7a905c1c997d1afc}

