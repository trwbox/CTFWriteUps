```txt
We're hot on the heels of catching this cyber gang but the closer we get the more damage they try to inflict onto the Barcelona tourism industry! This time, they've hacked into a large international bank's mobile application. Customers of the bank are complaining they can't see their current balance. Intern, help customers retrieve their balances so they can continue to spend their money during their well-earned holidays!
```

Looking at the network traffic, the app is doing a post request with a token to retrieve the data, with the balances page being 404 not found. Sending a post request to the main page with the token will show there are 3 links availble and not just the 2 in the app. The thrid is get-accounts, which after sending a post request with the same token gets the accounts and the flag ```postD4ta_w1zard```