#!/usr/bin/python3
def uppercase(input_str):
    result = ""
    for char in input_str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}\n".format(result), end="")
