---
layout: writeup
title: sp00kyma5k
---
# sp00kyma5k

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

Over the weekend after the competition, I looked more into cracking the passwords using a GPU to decrease the time needed. At first I tried to get john to use the NVIDIA GPU in my laptop, but was struggling with weird errors that caused things to break. So I decided to switch over to using hashcat instead since I read online it had an easier job working on a laptop, after getting a few drivers installed it just worked with the GPU for the benchmarks. I then dug into the man pages of hashcat, since it requires more specifics in the command structure to run properly. I ended up using the command ```hashcat -a 3 -m 500 masks.txt ?l?l?d?d?u?u?s --username --show```. This command uses hashcat attack mode 3 which is brute force with a specified mask, which I used the same mask as for john. The -m 500 tells hashcat it is a unix based md5+salt hashes that are being loaded in. --username and --show ignore the starting username and show the username with the cracked password respectively. Running this on my laptop, it took just over 15 minutes to crack all 3 passwords, which is a dramatic reduction in total time needed compared to CPU only cracking, and would have saved us a lot of time at the competition. I'm definitely glad that I learned about hashcat and how to get it use my GPU to speed up future times that I need to crack passwords

Final cracked hashes from hashcat

```txt
alice:$1$xbl0l1zU$Ur0MUnbko2XgpXhVxZ3430:bl00DY.
bob:$1$slIIXSsY$Jsu0vJERe06py7SmG1rbC1:gh05TS!
eve:$1$b8YPC.ff$v3xunqpTNTy6IgvJu1yZO1:wr41TH~
```
