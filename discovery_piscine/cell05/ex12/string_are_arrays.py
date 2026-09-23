"""String Are Arrays"""
from sys import argv
if len(argv) == 2:
    string = argv[1]
    z_count = string.count('z')
    if z_count > 0:
        print('z' * z_count)
    else:
        print("none")
else:
    print("none")
