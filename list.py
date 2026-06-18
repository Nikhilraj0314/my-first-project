fruits=["apple","banana","cherry","avocado","blueberry"]
list=[]
for fruit in fruits:
    if fruit[0]=='a' or fruit[0]=='b':
        list.append(fruit)
print(list)