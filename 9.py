list= ["Hi there", "Go", "I love Python", "OK fine"]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        count=0
        for ch in list[i]:
            if ch ==" ":
                count=+1
        count1=0
        for ch in list[j]:
            if ch==" ":
                count1=+1
        if count>count1:
            list[i],list[j] = list[j],list[i]
print(list)     