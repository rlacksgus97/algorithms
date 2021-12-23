t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    priority = [(p, i) for i, p in enumerate(priority)]

    count = 0
    while priority:
        if priority[0][0] == max(priority, key=lambda x: x[0])[0]:
            count += 1
            if priority[0][1] == m:
                print(count)
                break
            else:
                priority.pop(0)
        else:
            priority.append(priority.pop(0))