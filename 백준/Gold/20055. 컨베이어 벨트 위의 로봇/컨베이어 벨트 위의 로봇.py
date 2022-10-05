from collections import deque
N, K = map(int, input().split())
A = deque(list(map(int, input().split())))
robot = deque([0 for _ in range(N)])

step = 1
while True:
    A.appendleft(A.pop())
    robot[-1] = 0
    robot.appendleft(robot.pop())

    for i in range(N-1, -1, -1):
        if robot[i] == 1:
            if i == N-1:
                robot[i] = 0
                continue
            if robot[i+1] == 0 and A[i+1] >= 1:
                robot[i] = 0
                robot[i+1] = 1
                A[i+1] -= 1

    if A[0] >= 1:
        robot[0] = 1
        A[0] -= 1

    count = 0
    for i in range(len(A)):
        if A[i] == 0:
            count += 1
    if count >= K:
        break

    step += 1

print(step)
