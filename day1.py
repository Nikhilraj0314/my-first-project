fruit=["apple","banana","cheery","avocado","blueberry"]
vowels="aeiou"
no_vowel=[]
for list in fruit:
    new_box=""
    for char in list:
        if char not in vowels:
            new_box=new_box+char
    no_vowel.append(new_box)
            
print(no_vowel)