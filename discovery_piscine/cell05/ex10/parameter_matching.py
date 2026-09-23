"""Parameter Matching"""
from sys import argv

if len(argv) == 2:
    param = argv[1]
    input_param = input("What was the parameter? ")
    if param == input_param:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")
