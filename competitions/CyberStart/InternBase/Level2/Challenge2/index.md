```txt
A large bank has refitted all of their vaults with the new SpinLock Extreme. As fancy as it sounds we believe it has a rather critical vulnerability, one we think the Yakoottees have been exploiting in a series of recent bank robberies.

The physical vault itself requires a special keycard to be inserted which, after checking the authenticity of the card, re-aligns the circular locking mechanism to unlock it and updates the interface to show it's unlocked. However, we believe that the organisation has been remote accessing the interface on the vault, and unlocking the vault by doing it in reverse: getting the interface to unlock, which unlocks the physical vault itself. If we can confirm the method, we'll be one step closer to understanding how this cyber gang operates!

Tip: Unlock the vault to get the flag.
```

Inspecting the page has a javascipt file that says circles need to be between -81 and -4 to unlock the vault. And describes how there is a turnCirlce function that cane be called to turn the lock. It also describes hwo the circles are stored in an array. So calling the function like turnCircle(circles[0], -81) and doing that for all the cirlces causes the lock to unlock giving the flag ```09vWL20jd3WrCIt8puFi```