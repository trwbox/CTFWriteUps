# Xorathrust

## Description

Read the script and solve the problem.

Demo Flag: KCTF{Fl4g_H3r3}

Author: fazledyn

## Other informationq

Value: 25 points

Files:

- [encrypt.py](./encrypt.py)
- [flag.enc.txt](./flag.enc.txt)

## Solution

This challenge was a rather basic XOR of the flag with constant. This can be seen in the encryption script on the line `each = chr(ord(each) ^ 0x66)` which takes each byte and XOR with 0x66. Due to the transitive property of XOR, we can XOR the encrypted flag with 0x66 to get the plaintext flag. This function can be seen in the [decrypt.py](./decrypt.py) file.

```python
# Temp variable for the flag
flag = ""

# Read the encrypted flag
with open("flag.enc.txt", "r") as infile:
    # Read the flag in from the file
    flag_enc = infile.read()
    # Iterate through the flag and xor it with constant from encrypt of 0x66
    for each in flag_enc:
        each = chr(ord(each) ^ 0x66)
        # Append the character to the flag
        flag += each

# Print the flag
print(flag)
```

This gets a final flag of `KCTF{ju5t_4_b45ic_x0r}`
