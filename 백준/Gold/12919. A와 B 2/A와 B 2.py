# 13:20 -
S = input()
T = input()
answer = False


def dfs(t):
    global answer
    if t == S:
        answer = True
        return
    if len(t) == 0:
        return
    if t[-1] == 'A':
        dfs(t[:-1])
    if t[0] == 'B':
        dfs(t[1:][::-1])


dfs(T)
if answer:
    print(1)
else:
    print(0)
