s = input()
alphabet = []
sum = 0
for a in s:
    if a.isalpha():
        alphabet.append(a)
    else:
        sum += int(a)
alphabet.sort()
for a in alphabet:
    print(a, end='')
print(sum)