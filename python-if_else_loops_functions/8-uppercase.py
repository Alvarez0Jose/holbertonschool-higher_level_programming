#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(chra) <= 122:
            upper = chr(ord(char) - 32)
        else:
            upper = char
        print("{}".format(upper), end="")
    print()
