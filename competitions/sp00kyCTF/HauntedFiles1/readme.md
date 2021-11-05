# Haunted Files 1

Given a file called redrum.7z. With a message about how a hacker "encrypted" all their files and that they were missing a text file and was wondering if we could find it for them.

Extracting this file will get you a 5 GB iso file full of nested folders and files. Running Pop!_OS I was able to use the disk tool to mount the iso file as a normal file system. Since we have a known plain text that is ```sp00ky{``` this will let us use a recursive grep search ```grep -r "sp00ky{"``` to find the text file that contains the flag at the path ```lim6tzdtk/ac1y8v/bfzzl.txt```. Which contained the flag ```sp00ky{ph4n70m}```.
