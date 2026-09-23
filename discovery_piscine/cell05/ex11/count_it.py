"""Count It"""
from sys import argv
if len(argv) > 1:
    print(f"parameters: {len(argv) - 1}")
    for param in argv[1:]:
        print(f"{param}: {len(param)}")
else:
    print("none")
