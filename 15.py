input = [("Alice", 85), ("Bob", 92), ("Charlie", 85), ("David", 92)]
input.sort()
swapped_list = []
for name , marks in input:
    swapped_list.append((marks,name))

print(swapped_list)
last_list = []
for marks , name in swapped_list:
    last_list.append((name,marks))
print(last_list)