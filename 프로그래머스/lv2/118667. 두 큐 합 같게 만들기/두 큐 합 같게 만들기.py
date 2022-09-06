from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    if (sum1+sum2)%2 == 1:
        return -1
    target = (sum1+sum2)//2
    cnt = 0
    while sum1 != sum2:
        if sum1 > sum2:
            x = q1.popleft()
            sum1 -= x
            q2.append(x)
            sum2 += x
        else:
            x = q2.popleft()
            sum2 -= x
            q1.append(x)
            sum1 += x
        cnt += 1
        if len(q1) == 0 or len(q2) == 0 or cnt >= 600000:
            return -1
        answer += 1
    return answer