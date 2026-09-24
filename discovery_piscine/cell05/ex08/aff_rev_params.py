"""Aff_Rev_Params"""
from sys import argv
if len(argv) >= 3:
    for param in argv[-1:0:-1]:
        print(param)
else:
    print("none")
