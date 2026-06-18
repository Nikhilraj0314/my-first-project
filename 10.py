arr=[1,3,5,7,3,9]
arr1=[3,5,5,8,9]
temp=[]
for i in arr:
    if i in arr1:
        if i not in temp:
            temp.append(i)
print(temp)