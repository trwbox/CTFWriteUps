# GETMe

## Description

Can you GET the flag from the API ?

[http://167.99.8.90:9009/](http://167.99.8.90:9009/)

## Other information

Value: 25 points

## Solution

This challenge had us getting a flag from an API. The title seemed like a hint at using an http GET method by just opening the link in my browser, so that was the first thing that I tried which ended up with this response:

```json
{
    "success": false,
    "message": "Sorry ! You can't GET it :P"
}
```

Seeing that I couldn't GET the flag, let's try something else. I tried sending an empty POST with postman. This got me the following response:

```json
{
    "success": false,
    "message": "You should send me a url !"
}
```

Still no success, but we are getting somewhere, I need to send it a url! I wasn't entirely sure how it wanted the url, so I thought I'd take a guess at using sending it a POST with `form-data`, and using the key `url` with any value you give it gets this response:

```json
{
    "success": false,
    "message": "Looking for flag ? Visit https://hackenproof.com/user/security"
}
```

Still no success, but now a link to follow to get the flag. Following the link redirects to login page, so after creating an account, and visiting the site again the flag was sitting at the bottom of the page.

Flag: ```KCTF{H4ck3nPr00f3d_bY_Kn16h75qu4d}```