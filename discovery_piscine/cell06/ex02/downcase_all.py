"""Downcase all"""
from sys import argv

def downcase_all(string):
    """Return the string in lowercase"""
    return string.lower()

if len(argv) > 1:
    for param in argv[1:]:
        print(downcase_all(param))
else:
    print("none")
