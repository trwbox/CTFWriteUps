```txt
Our Dutch office recently bought a new Internet of Things (IoT) connected fridge. However, the temperature settings have been widely fluctuating as of late. All agents are currently out in the field and too busy to fix the problem.

We know there is a remotely accessible technician's page where fridge settings can be modified, and that the fridge's login page isn't very secure. It was easy enough to find the username and password, but the form still has some very lazy extra protection. Intern, can you see if the rumours are true, fix our fridge, and help us verify this reported security vulnerability?

Tip: Successfully login to get the flag.
```

Upon inspeciting the the page, you could look at the password field and find the default value is ```CoolUberFridge1000```, and that the login button has the HTML tag of disabled. Removing this tag let's you login as admin with the default value in password. Doing so gets you the flag of ```XP0zXyvy6Qs2CBybkj5n```