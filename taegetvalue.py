number=[2,4,3,7,1,5]
target=6
for i in range(len(number)):
    for j in range(i+1,len(number)):
        if number[i]+number[j]==target:
            print((number[i],number[j]))
# Q9