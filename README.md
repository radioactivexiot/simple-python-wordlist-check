# simple-python-wordlist-check
A python script simulating a brute force password guessing attack. 

It requires a file path to a wordlist (such as rockyou.txt)
It will then iterate upon the words in the wordlist with your input, checking each word against the wordlist.
If the word is found it will output the password that it matched it against and how long it took using the time module.
If it isn't..congratulations! Your password isn't vulnerable (atleast against the wordlist you're checking it against).

This checker can be used with files such as rockyou.txt to check whether certain passwords are vulnerable, or even be implemented in a password input environment to ensure that a user does not enter a vulnerable password.
