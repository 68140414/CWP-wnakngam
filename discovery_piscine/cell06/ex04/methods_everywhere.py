"""Methods Everywhere"""
from sys import argv

def shrink(string):
    """Shrink to the first 8 characters"""
    return string[:8]

def enlarge(string):
    """Append 'Z' to make total of 8 characters"""
    return string + 'Z' * (8 - len(string))

if len(argv) > 1:
    for param in argv[1:]:
        if len(param) >= 8:
            print(shrink(param.replace("'", '')))
        else:
            print(enlarge(param.replace("'", '')))
else:
    print("none")
