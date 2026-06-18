word=["eat","tea","tan","ate","nat","bat"]
same =[]
for anagram in word:
    group=[]
    for words in word:
        for i in anagram:
            for j in words:
                if(i==j):
                    break
            else:
                group.append(words)
    if(group not in same):
        same.append(group)
print(same)
