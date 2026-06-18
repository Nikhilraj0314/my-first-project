s="hello world"
rev_string=""
for rev in range(len(s)-1,-1,-1):
    rev_string+=s[rev]
print(rev_string)