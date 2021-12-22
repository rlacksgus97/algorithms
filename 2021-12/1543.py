doc = input()
word = input()
idx = 0
count = 0

while idx+len(word) <= len(doc):
    if doc[idx:idx+len(word)] == word:
        count += 1
    idx += len(word)

print(count)

#fail