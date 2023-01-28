# Fan

## Description

Do you know how many programming language are there. As a hacker you should know all of them. Don't worry. I am just kidding. But do you know how programming language are well understood by computer? One of our senior researcher found this but he can't remember where he found it as well as what was it. You should help him otherwise he will laugh at you thinking you are a noob. Prove him you are pro. I know you can do it. Just tell me what is the message and I will pass it to him.

Demo Flag: KCTF{::::something:::::here}

Author: Al Arafat Tanin | rng70

## Other information

Value: 250 points

Files: [fan](./fan)

## Solution

This challenge was an interesting one. We were given this text file that had hints in the contents that it was somehow related to python, but unsure exactly how. After some more digging we saw that it was python assembly of some kind. [This is the disassembler tool we think was used to generate the file](https://docs.python.org/3/library/dis.html).

After trying to use the tool to take this assembly and either compile, or run it, we just couldn't figure it out. So I decided the best move was to just completely reverse the source from the assembly.  Starting from the first block there were a set of statements that looked similar to this:

```python
 25:          16 LOAD_CONST           (<code object define_both at 0x7fbea9699540, file "chall.py", line 25>)
              18 LOAD_CONST           ('define_both')
              20 MAKE_FUNCTION        (Neither defaults, keyword-only args, annotations, nor closures)
              22 STORE_NAME           (define_both)
```

This is a block that describes how a new function was defined, the name of the function (define_both), and on what line of the file it was defined (line 25). All of the instructions had line numbers that associatted with instruction made reversing the file dramatically easier, as I was confident in my placement of the code. After going through all the higher level definitions, I got the structure of the file looking like this:

| Line | Function Name |
| :--- | :--- |
| 1 | define\_false |
| 19 | define\_true |
| 25 | define\_both |
| 40 | if \_\_name\_\_ == "\_\_main\_\_": |
| 41 | static array |
| 42 | print flag |

The next step after this was filling out all the functions code with the instructions that were associated with them. All the functions had a header that looked like this prior to the instructions:

```python
# Method Name:       define_false
# Filename:          chall.py
# Argument count:    1
# Keyword-only arguments: 0
# Number of locals:  7
# Stack size:        4
# Flags:             0x00000043 (NOFREE | NEWLOCALS | OPTIMIZED)
# First Line:        1
```

This gave me the information I needed to fill out the functions with the correct number of arguments. I then started looking at the instructions. There were some that were rather easy to understand what was happening like the first instruction in the define\_false function that just creates an empty list and stores it in a variable lstr:

```python
  2:           0 BUILD_LIST           0
               2 STORE_FAST           (lstr)
```

Not all the instructions were as easy to understand, there was assembly like this used to create a for loop:

```python
  5:          12 SETUP_LOOP           (to 126)
              14 LOAD_FAST            (s)
              16 GET_ITER
         >>   18 FOR_ITER             (to 124)
              20 STORE_FAST           (c)
```

Thinking through this code, the SETUP\_LOOP instruction is used to create a loop, and then the FOR\_ITER and GET\_ITER instuctions are used to iterate. Looking at the code, you can tell the variable being iterated over is `s` as it is being loaded, and `c` is the variable being used to hold the iterating item since it is being stored too. This code also show how the code designates that an instuction can be jumped to with the `>>` symbol. This is used for where the loop jumps back to. It is also shows what it looks like to jump somewhere else in the code with the chunks like `(to 124)` which is the instruction number that will be jumped to when the jump is taken. So let's take a look at 124 and 126 since this is where this code jumps to.

```python
 16:     >>  114 LOAD_FAST            (packed)
             116 LOAD_FAST            (c)
             118 INPLACE_ADD
             120 STORE_FAST           (packed)
             122 JUMP_ABSOLUTE        (to 18)
         >>  124 POP_BLOCK

 17:     >>  126 LOAD_FAST            (packed)
             128 RETURN_VALUE
```

This code shows a couple things with line 17 showing what returning from a function looks like, by loading a variable, then calling the return instruction. Line 16 shows the final line of the for loop from above. With the actual line contents only being executed based on an earlier if statement. But it is a good line anyway that shows a few things, how when exiting the loop the POP\_BLOCK instruction is called freeing up the iterator `c` and how the loop jumps back to the beginning of the loop with the JUMP\_ABSOLUTE instruction. It also shows how you can create an arithmetic line from the instructions with line 16 showing how the variables `packed` and `c` are being laoded together, then an INPLACE\_ADD occurs which shows that one of the loaded variable is going to be where the result of the operation is stored, then a STORE\_FAST with `packed` shows that line most likely looked similar to one of these:

```python
packed = packed + c
packed += c
```

Jumping up a little and taking a look at the assembly for an if statement:

```python
 13:     >>   88 LOAD_FAST            (c)
              90 LOAD_ATTR            (isdigit)
              92 CALL_FUNCTION        (0 positional arguments)
              94 POP_JUMP_IF_FALSE    (to 114)
```

This assembly above shows how the first thing loaded is the variable `c`, then the attribute `isdigit()` is loaded and called with CAL\_FUNCTION. The value returned is then checked with POP\_JUMP\_IF\_FALSE, where it will jump to the instruction number 114 if the value is false, otherwise it just continue executing the current code.

With these basic ideas, I was able to get the vast majoirty of the code reversed with ease, however there are a few scenarios that I want to point out that I struggled with understanding and took a couple tries to figure out. 

```python
 41:          32 LOAD_CONST           ('chr(75)chr(67)chr(84)chr(70)chr(123)')
              34 LOAD_CONST           ('chr(115)chr(105)chr(85)chr(85)chr(85)')
              36 LOAD_CONST           ('chr(109)chr(69)chr(51)chr(115)chr(115)chr(105)')
              38 LOAD_CONST           ('chr(105)chr(115)')
              40 LOAD_CONST           ('chr(103)chr(48)chr(79)chr(97)chr(116)chr(125)')
              42 BUILD_LIST           5
              44 STORE_NAME           (s)
```

The first being how an array with multiple elements is created. It first loads the constants, then runs the list creation, and storing the list in a variable. My first thought was the list would be created with the first constant, then the second constant would be appended to the list, and so on. However, this is not the case. The list is created in a reverse order where the last constant loaded is the first element in the list. The next section I took a few tries to understand was this packing section of the code

```python
 22:          14 LOAD_FAST            (res)
              16 LOAD_GLOBAL          (str)
              18 LOAD_GLOBAL          (len)
              20 LOAD_FAST            (packed)
              22 CALL_FUNCTION        (1 positional argument)
              24 CALL_FUNCTION        (1 positional argument)
              26 LOAD_CONST           ('[:]')
              28 BINARY_ADD
              30 LOAD_FAST            (packed)
              32 BINARY_ADD
              34 INPLACE_ADD
              36 STORE_FAST           (res)
              38 JUMP_ABSOLUTE        (to 10)
         >>   40 POP_BLOCK
```

This code is used to pack a string. My firs thought while looking at this code was to start rebuilding the line from the bottom up. With the INPLACE\_ADD of `res` starting the line `res = something + res` like so, then another addition of the value of `packed` to become `res = packed + res`. With the next part looking to me like it is calling the function `str()` on the result of the function of `len(packed)` then using the python splicing operator to get `str(len(packed))[:]` resulting in the final string being `res += str(len(packed))[:] + packed`. However, this is not the case. The code is not using `[:]` as an operator, but as a string constant with the BINARY\_ADD on 28 adding the `str(len(packed))` and the constant together getting the line `res += str(len(packed)) + '[:]' + packed + res`. This was the last line that I had to get sorted out to have the fully complete [source code](chall.py) used to generate the assembly. Which I then ran in python and got the output of `:::::KCTF{:::::siUUU::::::mEssi::::::::::::::::::::::::::::::::is::::::gOat}`

Taking a look at the description this appears to a correct falg since they had a large number of colons in their flag too, so I removed the leading `:` to get `KCTF{:::::siUUU::::::mEssi::::::::::::::::::::::::::::::::is::::::gOat}` which was the correct flag.