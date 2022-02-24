---
layout: labs
title: Install OpenLDAP
---
# CYBE230 Lab 6 - Install OpenLDAP

At the time of starting this lab, we had started talking about directory services, and how they can be used to store information about users. We also talked about how ideally this lab would involve setting up Windows Active Directory and LDAP to see the differences, but for licensing, and processing plower reasons. We only installed LDAP, and spent part of the lab comparing the process with how it would work in Windows Active Directory.

To set up the ldap server we set up slapd as the backend daemon for running the ldap process, and ldap-account-manager with as the gui to interact with the daemon from a web interface. In the web interface we added all the users,and added them to their proper groups. Along with setting things, like what to store in the local home directory, vs on the server, the shell to use, and login rules.

After we setup the server with all the proper accounts, we created another Ubuntu Desktop system that used the ldap authentication for all of its users. We set up the desktop to get the passwd, group, and shadow information from the ldap server using the linux pam authentication. We then tested the machine to see if it was set up correctly, and if it was we were able to login with all of the accounts we created.
