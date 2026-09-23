"""Free Range"""
from sys import argv
if len(argv) == 3:
    num1 = int(argv[1])
    num2 = int(argv[2])
    arr = [x for x in range(min(num1, num2), max(num1, num2) + 1)]
    print(arr)
else:
    print("none")
