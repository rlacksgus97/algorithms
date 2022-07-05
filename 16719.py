def findMin(s, check):
    index = 0
    minAlpha = s[0]
    for i in range(1, len(s)):
        if minAlpha >= s[i] and not check[i]:
            index = i
            minAlpha = s[i]
    return index

def printAnswer(s, check):
    for i in range(len(s)):
        if check[i]:
            print(s[i], end='')
    print()

s = input()
check = [False for _ in range(len(s))]
index = 0
for _ in range(len(s)):
    index = findMin(s[index:],check)
    check[index] = True
    printAnswer(s, check)
