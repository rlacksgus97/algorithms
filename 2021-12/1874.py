n = int(input())
stack = []
answer = []
idx = 0

for _ in range(n):
    x = int(input())
    while idx <= x:
        stack.append(idx)
        idx += 1
        answer.append('+')
    if stack[-1] == x:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(answer))