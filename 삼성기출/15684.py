n, m, h = map(int, input().split())
ladder = [[0 for _ in range(n)] for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1

def play(ladder):
    for j in range(n):
        line = j
        for i in range(h):
            if ladder[i][line] == 1:
                line += 1
            elif ladder[i][line-1] == 1:
                line -= 1
        if line != j:
            return False
    return True

def setup(ladder, count, x, y):
    global answer
    if play(ladder):
        answer = min(answer, count)
        return
    if count == 3:
        return
    for i in range(x, h):
        if i == x:
            s = y
        else:
            s = 0
        for j in range(s, n-1):
            if ladder[i][j] == 0 and ladder[i][j-1] == 0:
                ladder[i][j] = 1
                setup(ladder, count+1, i, j+2)
                ladder[i][j] = 0

answer = 4
setup(ladder, 0, 0, 0)
if answer == 4:
    answer = -1
print(answer)