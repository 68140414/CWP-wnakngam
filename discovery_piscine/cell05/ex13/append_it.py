"""Append it"""
from sys import argv
if len(argv) > 1:
    for param in argv[1:]:
        if param[-3:] != "ism":
            print(f"{param}ism")
else:
    print("none")
