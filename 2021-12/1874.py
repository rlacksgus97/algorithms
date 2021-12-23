n = int(input())

idx = 1
stack = []
answer = []
for _ in range(n):
    x = int(input())
    while idx <= x:
        stack.append(idx)
        answer.append('+')
        idx += 1
    if stack[-1] == x:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(answer))