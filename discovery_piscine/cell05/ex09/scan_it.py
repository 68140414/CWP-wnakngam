"""Scan It"""
from sys import argv
if len(argv) == 3:
    keyword = argv[1]
    string = argv[2].split()
    print(string.count(keyword))
else:
    print("none")
