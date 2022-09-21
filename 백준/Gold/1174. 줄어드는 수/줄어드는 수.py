N = int(input())
answer = 0


def dfs(num, length, result):
    global answer
    if len(result) == length:
        answer += 1
        if answer == N:
            print(result)
        return
    elif len(result) < length:
        for i in range(num):
            dfs(i, length, result+str(i))


for l in range(1, 11):
    for i in range(10):
        if answer < N:
            dfs(i, l, str(i))

if answer < N:
    print(-1)
