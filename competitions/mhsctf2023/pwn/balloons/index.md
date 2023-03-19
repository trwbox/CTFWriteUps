# Feb 01 - Balloons

## Description

Starting off with a bang (pop)! I ordered a bunch of Valentine's Day-themed balloons, and I'm so excited about them! Here's the portal I use to track my order.

Look for "valentine.txt."

Author: Manav (0xmmalik)

## Other Information

Value: 2 coins

Files: [balloons.py](balloons.py)

Link: A server and port you connect to with netcat

## Solution

Taking a look at the code, this is python2 code, which is using the `input()` function. Looking into the python manuals this function is highly vulnerable to exploitation if there is user input. This is because the input function is equivalent to `eval(raw_input(user_string))`. This means that if the user inputs a string, it will be evaluated as python code. This is a huge security flaw, and can be used to execute arbitrary code. Thinking through this and what I could do to get a file of the system, I used the `os` module to execute the `cat` command to read the `valentine.txt` file. The payload I used was `__import__("os").system("cat valentine.txt")` which uses the builtin `__import__` function to import the `os` module, and then executes the `system` function with the argument of `cat valentine.txt`. This resulted in the flag being printed out. What did throw me for a loop for a while was the period in the description of the challenge, which I thought was a period in the file name, until I tried it without the period and it worked.

Flag: `valentine{0ops_i_go7_hydrog3n_ball00n5_NONOWHEREAREYOUGOINGWITHTHATLIGHTER}`
