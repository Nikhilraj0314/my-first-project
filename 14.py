input = [100, 4, 200, 1, 3, 2]
input.sort()
count=1
max_count=1
for i in range(1,len(input)):
    if input[i] == input[i-1] +1:
        count+=1
    elif input[i]!=input[i-1]:
        count=1
    if count > max_count:
        max_count=count
print(max_count)