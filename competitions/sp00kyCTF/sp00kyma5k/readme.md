# sp00ky ma5k

Before the competition there was an announcement that there was going to a be a physical prize for the team that completed the challenge first. Our team before the competition began decided we wanted to win the prize, so as soon as we had enough points immediately bought both hints for a combined 50 points making the challenge worth no points.

To start of the challenge we were given this hint with **_sp00KY!_** in bold and italicized.

```txt
Everyone loves a good sp00KY! mask on halloween but I can never decide between one so I end up buying 7. 
Anyway, I don't want to wear the same mask as my L33T Hack3r friends 
but I cant seem to crack the code to figure out what masks that they are planning to wear. 
Help me crack the code and you can have a mask from my extensive collection.

note there are three flags in this file but they do not have a flag tag
you must append them with an underscore using the following format.
submit sp00ky{<alicePlaintext>_<bobPlaintext>_<evePlaintext>} 
```

and a .txt files named masks.txt which contained the following password hashes in the same format as the /etc/shadow file on most linux systems. These specific hashes are md5 with salt which is signified with $1$ right after the username

```txt
alice:$1$xbl0l1zU$Ur0MUnbko2XgpXhVxZ3430
bob:$1$slIIXSsY$Jsu0vJERe06py7SmG1rbC1
eve:$1$b8YPC.ff$v3xunqpTNTy6IgvJu1yZO1
```

<details><summary>Hint 1 (Click to see)</summary>
There are alot of sp00KY! phrases around 7 characters long...
<br>
</details>

<details><summary>Hint 2 (Click to see)</summary>
I used to know this guy John who was great with hases like this, he really loved --mask.
<br>
</details>

With both these hints I got john-the-ripper downloaded, and started research how to use the --mask flag. Finding the john manual was very helpful, and showed exactly how to create a mask. After reading the document I ended up using a mask of ```?l?l?d?d?u?u?s``` which starts with 2 lowercase letters signified by ?l, 2 digits signified by ?d, 2 uppercase letters signified by ?u, and 1 symbol signified by ?s. This made the final command I ran to be ```john-the-ripper --mask=?l?l?d?d?u?u?s masks.txt```. This took about 45 minutes to complete on my system, but this was while using the CPU, so for the first 15 minutes or so I attempted to get john to use the GPU in my system with no luck figuring it out, but put that on the back burner to figure out after the competition was over and let it finish cracking.

This got me the three passwords being ```alice:bl00DY.```, ```bob:gh05TS!```, and ```eve:wr41TH~```. We did end up being the first team to complete the challenge by just a few minutes, and we got the prize of anonymous masks for the whole team.
