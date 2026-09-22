"""Up to 25"""
start = int(input("Enter a number less than 25\n"))
if start > 25:
    print("Error")
else:
    for i in range(start, 26):
        print(f"Inside the loop, my variable is {i}")
