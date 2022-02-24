---
layout: labs
title: Packages and DNS
---
# Lab 5 - Packages and DNS

This is the lab that I personally struggled the most with, as there are a lot of moving components outside of the infrastructure I had direct control over. This presented challenges when a mistake was made, but still acted correctly. This led to the error being propagated repeatedly, until the time to live had expired.

In this lab we installed some packages, and configured DNS using a bind9 package. At this time, we also talked about how to verify package integrity using debsums. Doing this we learned that the sl binary had been modified, and we reinstalled it to match the correct debsum.

When we got to setting up the DNS. We set up a split DNS with one server serving as the DNS server for the internal network, and another server serving as the authoritative DNS server to the ISEAGE environment for our given domain.

The external DNS server was set up the forwarder for the ISEAGE environment, then set up the local zones for both forward and reverse lookups on on the addresses. This is where I had an issue in this lab. I created an incorrect forward lookup, that pointed to an unused ip address. In doing this, the change was cached by the forwarder, and kept sending that response for the 3 days that it was set to be cached for. After that time, it re-cached the data from the authoritative server, and it was no longer an issue. To figure out the issue it involved a lot of talking with TAs of the class, and the professor and digging into the distributed nature of DNS. I'm glad I had the issue though as it helped me understand how DNS is able to work relatively seamlessly and quickly, while being so distributed.

After that, we set up the internal DNS server in the same way, but added some more addresses that were only available within the local network. We then set the DNS server as the default server for the firewall, and the traffic behind the firewall to use, to know we are actively using that as the primary DNS server for the internal network. For this server we also had to set up a port forwarding rule to let the automated checker verify that DNS was working properly, with a rule that only allowed traffic on port 53 from the specific IP.
