# Mission Possible

## Description

Welcome back agent, we've got a doozy for you.

This mission, If you choose to accept,  will require you to crash the banks security cameras just long enough for one member of your team to slip into the lock box, take a picture of the flag, and get out before it comes back online. The only intel on this target is that they use [TENVIS TH661](https://manuals.plus/tenvis/th661-wifi-hd-p2p-pan-ip-camera-manual) security cameras

The security camera is on the wifi network `Almond`.

Any questions? Didn't think so. Good luck agent, we believe in you.

EDIT:
hint1 will give you the IP of the camera

## Other information

Value: 100 points

Hints
| Cost | Hint |
|------|-------------|
| 10 | <details> <summary> Click to view hint </summary> the camera's IP is 10.10.10.104 </details> |

## Solution

This challenge required turning off a security camera feed, so that you could sneak by and grab the precious flag without being seen.  You told the model of the camera was `Tenvis TH661`, and that is was the `Almond` WIFI network. The first thing I would do is use nmap something like `nmap -T5 -p- 10.10.10.1-255` since that was subnet once connected to WIFI network, which scans all the ports over the whole subnet since it was most likely pretty empty being only for this CTF. This would get the ip of the camera and what ports it had open. Since many embedded devices are just very lightweight Linux computers, that don't get updated often, they can have known vulnerabilities available for their entire lifetime if they aren't manually updated. After finding the IP, I would then look for known vulnerabilities with some google search like `tenvis "th661" vulnerability`. This uses the quotation google dork to require the search result to have that camera model. This google search has the first result being a super generic article about not exposing cameras to the internet. However the second result is a pdf slide deck from a conference. In this slide deck, about general IOT Hacking there is a slide with the title of the camera name describing a buffer overflow in the parsing of the http header leading to the overwriting of the stack pointer and getting code execution. I Specifically it was slides 11-12 of this [Slide Deck](https://published-prd.lanyonevents.com/published/rsaus19/sessionsFiles/13780/SBX1-R2%20-%20Hello%20-%20It_s%20Me,%20Your%20Not%20So%20Smart%20Device.%20We%20Need%20to%20Talk.pdf). If you attempted to run this exploit, you would unfortunately not get a telnet daemon to start, but you would cause the camera to crash. You could then watch as the camera began it's reboot sequence where it tests all the motors, and since this takes ~1-2 minutes you have just enough time to sneak by and grab the flag. The flag was `sp00ky{Im_In_B-)}`.

## Extra

I tried for a while to get the buffer overflow working from the slide working, it only ever (presumably) crashed the web server. When it crashed the web server, it seems like there is something running that will force reboot the camera if this happens to prevent the server from being constantly down. During this reboot, the camera doesn't display video, and does a motor calibration checking all axis, giving you ~1-2 minutes where the camera is completely blind. We wanted you to find this slide deck, and then send a request that would cause the crash allowing you to "sneak up and take what was in the secret box". I also think the full code execution buffer overflow is still probably possible, but we have a slightly different camera than from the talk, so a new payload would need to be created for this camera. Opening up the camera there appears to be UART header, so maybe hooking up to that can get me a shell I can debug on that would help write the new exploit. I think another possibility, is padding the code with a NOP slide, in case the memory address is just offset weird, but have not got around to doing that yet.
