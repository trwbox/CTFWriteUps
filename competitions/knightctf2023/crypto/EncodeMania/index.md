# Encode Mania

## Description

Encoding random stuffs is so cool! I just want to encode it over and over and over again ...

Demo Flag: KCTF{fl4g_h3r3}

Author: lolipop

## Other information

Value: 150 points

Files:

- [encode_mania.py](./encode_mania.py)
- [encode_mania.txt](./encode_mania.txt)

## Solution

Taking a look at the source code this section stands out;

```python
for _ in range(12):
    option = randint(0, 3)
    encrypted_flag = encrypt(encrypted_flag, option)
```

This takes the flag and repeatedly encodes it with either base64, base32, base16 or base16. With enough trial and error I felt like I could have gotten the flag, but decided to automate into something that I could just run and analyze the output. For the script what I did was take the intital value then attempt to decode it with all 4 options, and if the deocding failed ignore it becuase it wasn't correct, but if the decoding was successful, save it to a list and repeat the process for the 12 times that I needed to. Since we knew the flag would be valid text, try and decode all the outcomes, and discards any that don't properly become text. I then decided to write all the values that came out of the decoding into different files, so I could hopefully just use a tool like grep to find the flag.This can be seen in [decode_mania.py](decode_mania.py).

That was however not needed, as after building the tool and running it, there was only a single value that was able to be decoded through all 12 iterations. That was the flag `KCTF{dfs_0r_b4u7e_f04c3}`