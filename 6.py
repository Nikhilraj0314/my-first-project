paragraph = "My name is nikhil my name is short"
words = paragraph.lower().split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] = word_counts[word] + 1
    else:
        word_counts[word] = 1
max_count = 0
for word in word_counts:
    if word_counts[word] > max_count:
        max_count = word_counts[word]
result = ""
for word in word_counts:
    if word_counts[word] == max_count:
        if result == "" or word < result:
            result = word

print(result)