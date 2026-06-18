s="listen"
a="silent"
a_list=list(a)
result="yes"
for i in range (len(s)):
    char=s[i]
    found=False
    for j in range(len(a_list)):
        if char==a_list[j]:
            a_list[j]=None
            found=True
            break
    if not found:
        result="no"
        break
print(result)    
