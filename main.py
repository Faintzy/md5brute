"""
@ A simple md5 decoder based on user wordlists
@ Coded by https://github.com/sudoGabriel

"""

import hashlib

thestr = input("[!] Enter a word for decrypt: ")
wordlist = input("[!] Enter the wordlist file name (.txt): ")

file = open(str(wordlist), "r")
words = file.read().split("\n")

n = 0

while n < len(words):

    hash = hashlib.md5(str(thestr).encode('utf-8')).hexdigest()
    word = words[n]
    wordhashed = hashlib.md5(str(word).encode('utf-8')).hexdigest()

    if hash == wordhashed:
        print("[!] ~~ " + word + " ~~ FOUND!!")
        break

    n = n + 1

print("[!] Hash not found")
