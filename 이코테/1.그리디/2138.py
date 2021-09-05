n = int(input())
now = list(map(int, input()))
goal = list(map(int, input()))

def check(cnt, state):
    if cnt == 1:
        state[0] = 1 - state[0]
        state[1] = 1 - state[1]

    for i in range(1, n):
        if state[i-1] != goal[i-1]:
            state[i-1] = 1 - state[i-1]
            state[i] = 1 - state[i]
            if i < n-1:
                state[i+1] = 1 - state[i+1]
            cnt += 1
    
    if state == goal:
        return cnt
    else:
        return -1

case1 = check(0, now[:])
case2 = check(1, now[:])

if case1 != -1 and case2 != -1:
    print(min(case1, case2))
elif case1 == -1:
    print(case2)
elif case2 == -1:
    print(case1)
else:
    print(-1)
