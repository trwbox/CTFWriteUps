# IT'S IN THE AIR?!?!

## NOTE: This is currently a work in progress, as I seemed to have misplaced things like my packet capture from the event.

## Description

While not required it is recommended to do [Pulling passwords from thin air](/competitions/sp00kyCTF2022/RealWorld/PullingPasswordFromThinAir/) challenge before attempting this challenge.

Back in my day, I remember the only thing humans were putting in the air were the chem trails. Now they have all these gosh darn radio waves flying around that keep hitting ne upside the head. At least most of them are encrypted gibberish, but this one dingus keeps sending their password every few seconds over basically plaintext.

The flag is the password being used to authenticate with the router on the `Almond` wifi network.

This challenge requires wifi adapters that go into monitor mode, if you do not have one the club has a few usb ones available.

## Other information

Value: 100 points

Hints
| Cost | Hint |
|------|-------------|
| 25 | <details> <summary> Click to view hint </summary> Wireshark struggles to monitor HTTP traffic with a wifi adapter in monitor mode. Maybe try use a different tool to create a packet capture? </details> |

## Solution

For this challenge, it describes how a device is authenticating with the router on the Almond Network. This wifi network ahs no password meaning that any data sent on it does not have encryption unless the protocol has encryption like HTTPS, and anyone can capture and look at the data being sent. To do this, you need a wifi card that can go into monitor and promiscuous mode, so that it lets you monitor all the traffic. I then use a tool set call `aircrack-ng` which has a variety of tools for capturing and cracking wifi. The tools that I am most interested in is `airmon-ng` which will change all the necessary setting automatically to put your wifi card into monitor mode. After running this, your wifi card will be in monitor mode, so you can monitor the traffic around you. The next thing I did was use Wireshark to try capture packets from the wifi card, but for some reason that was only capturing 802.11 frames, and not anything else. So I switched back to a tool from the aircrack-ng suite, `airodump` which is a tool for capturing packets on a wifi card in monitor mode. After capturing about 1 minutes worth of packets, I thought it was likely I had captured at least 1 useful packet. 

I took that packet capture from `airodump` and loaded it into Wireshark, with the description recommending the previous challenge, I was guessing it was a similar idea, so searched for HTTP packets, and there is a device making very similar HTTP requests to the router. It was again in the authorization header, with a basic format `YWRtaW46c3AwMGt5e2dob3N0c19pbl90aGVfYWlyfQ==` taking this from base 64 again gets `admin:sp00ky{ghosts_in_the_air}` which is the flag. Another thing I noted is that this request is going to a different endpoint on the router, the first went to the root, but this request is going to `advanced/system_command.shtml`.

## Extra

There were actually 2 devices authenticating against the router at hat endpoint, and raspberry pi running a bash script, and an ESP32. I have included the code for the ESP32 if someone wants to see more information about how the request can be created by not a human, or wants to try this on their own.
