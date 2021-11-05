---
layout: writeup
title: Haunted Files 2
---
# Haunted Files 2
 
This is a continuation of Haunted Files 1 with the description of: ```Hey I also forgot to mention, I am missing a picture of the group from last years exorcism festival. Please let me know if you can find it. I would really appreciate it.```

The first thing that I tried to do was grep for files ending in .jpeg, .jpg, .png, and .gif Hoping that there was just a file hidden somewhere with the correct ending on it. That was unsuccessful however. My next best guess was that they kept the entire information from the picture and only changed that ending to .txt. After some thinking I worked my way to a 1 line bash script that uses find to get every file in the directory recursively, and run the file command on them. ```find . -type f -exec file '{}' \;```. I then piped it into a few instances of grep looking for common picture headers of JPEG, PNG, and GIF. After some time running eventually I found a file with a matching header using the JPEG search. ```find . -type f -exec file '{}' \; | grep JPEG```. The file ended up being at ```/asydv6ypzo/o2y42ninx.txt```, changing the file name back from .txt to .jpg you get the image below with the flag.

![ImageFile](o2y42ninx.txt)