a = "abcabcbb"
longest=""
for i in range(len(a)):
    temp=""
    for j in range(i,len(a)):
        if a[j] not in temp:
            temp+=a[j]
        else:
            break
        if len(temp)>len(longest):
            longest=temp
print(longest) 
# q12