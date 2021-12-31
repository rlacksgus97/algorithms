n = int(input())
coin = list(map(int, input().split()))

coin.sort()
goal = 1
for c in coin:
    if goal < c:
        break
    goal += c

print(goal)

#fail