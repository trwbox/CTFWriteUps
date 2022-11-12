# They're on the move!!

## Description

About 25 minutes after I got the first picture. The same person sent another picture telling me they had moved. Can you help me find them again? The flag is in the same format so `123 University Ave` would be `sp00ky{123UniversityAvenue}`
![Location2.jpg](Location2.jpg)

## Other information

Value: 200 points

Included files: [Location2.jpg](Location2.jpg)

Hints

Hint 1: Cost 25 points
<details> <summary> Click to view hint </summary> At least we can tell they didn't leave the country in those 25 minutes with the flag in the background </details>

Hint 2: Cost 20 points
<details> <summary> Click to view hint </summary> That's a really pretty color blue on the cart return. I wonder where I have seen that color before. </details>

Hint 3: Cost 25 points
<details> <summary> Click to view hint </summary> Weird, I can see yellow parking lines when I would expect white ones for this parking lot. I wonder if that would be of help? </details>

Hint 4: Cost 50 points
<details> <summary> Click to view hint </summary> They sent the image only 25 minutes after the first, they can't have gotten very far. Maybe a 20 minute drive from the last picture? </details>

Hint 5: Cost 30 points
<details> <summary> Click to view hint </summary> What's that thing in the dead-zone mirror? Big black fences, piles of materials, maybe some plants. Seems rather permanent with its size. </details?

## Solution

Here we are given another image, and told to find the address again. This is significantly harder, as there is even less to go on. The description says that this image was sent ~25 minutes after the first one, so we can assume that the person could not have gone more than ~25 minute drive away. So I started with a looking at clues in the images, the first thing that stands out to me is the big blue shopping cart receiver, which pin points me in a WalMart parking lot. Doing a quick google search for WalMarts near the first location, there are a few in a 20 minute drive making pinpointing an exact location hard.

Digging a little more into the image, there is an American Flag in the background, and there are yellow painted parking lines. So my next plan was to hop into street view and look to see which WalMart parking lots, I could see yellow lines, and an American Flag. Surprisingly, this was more than 1 WalMart in the area. So going back to the images, I wanted to see if there was anything else that could be a distinction. And then I saw it in the rear-view mirror. That tall black fencing, and the outdoor metal tables. There is a permanent garden center on this WalMart. Having already narrowed it down to a few WalMarts, I looked to see how many had a garden center, and it was just one. This one to be precise [Street View of said WalMart](https://www.google.com/maps/@35.6621469,-78.4967309,3a,15y,27.11h,89.94t/data=!3m6!1e1!3m4!1s4J-TyTjd_gpAaa-7_aC3Ow!2e0!7i16384!8i8192). If the background on there is an American Flag, there are yellow parking lines, it has a garden center, and all within a 25 minute drive from the last location. The WalMart super center at `805 Town Centre Boulevard`. This makes the flag `sp00ky{805TownCentreBoulevard}`.

Since this was an OSINT challenge there were a few possible flags:

```txt
sp00ky{805TownCentreBlvd}
sp00ky{805TownCentreBoulevard}
```

## Extra

This challenge, and [Seeking Someone](/competitions/sp00kyCTF2022/OSINT/SeekingSomeone/) are actually real life times that I did OSINT, these images were sent by a friend of mine, and made a joking comment about guessing where they were. So, instead of making a guess, I thought I'd see if I could drop a pin on his exact location which led to the creation of these challenges.
