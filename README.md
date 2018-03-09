# qmail-alias-pycontrol
Python script to control qmail alias entries.

I use aliases and this script as a little helper for adding aliases to my very
own spamlist. I use my own domain for receiving mails and I create an alias for
every service I sign up to. So if I receive spam to one of thosee aliases, I
know who gave away my address and I can handle further mails to that alias (so
far I bounce and erase them).

To handle an alias with qmail, I need to create a file for every alias, 
containing the instructions for qmail on what to do with a mail addressed to
this alias. I made this script to automate this process. 

I used python because it is the only language I know a little, but I am for sure
not a programming pro. Feel free to share productive feedback.
