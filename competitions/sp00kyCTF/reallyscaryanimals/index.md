---
layout: writeup
title: reallyscaryanimals
---
# reallyscaryanimals

We were given a plain text file with no extension that included the values of N = 1079, e = 43, and Ct which was an array of values. Those names immediately made me think of an RSA encryption type of problem. Since N is small enough that made finding it's prime factors easy with just a google search. With that I could use [dcode.fr](https://www.dcode.fr/rsa-cipher) to go through the values of Ct decrypting them one at a time to get a string and a flag of ```sp00ky{RSA_SHMRSA_AM_I_WRITR??}```
