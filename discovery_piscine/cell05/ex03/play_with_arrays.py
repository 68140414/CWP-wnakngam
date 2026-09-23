"""Play with Arrays+=2"""
arr = [2, 8, 9, 48, 8, 22, -12, 2]
print(arr)
new_arr = [x + 2 for x in arr if x > 5]
new_set = set(new_arr)
print(new_set)
