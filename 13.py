input="pwwkew"
same=""
for i in range(len(input)):
    diff=""
    for j in range (i,len(input)):
        if input[j] not in diff:
            diff=diff+input[j]
    else:
        break
        if len(diff)>len(same):
            same=diff
print(same)
