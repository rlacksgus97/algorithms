n = int(input())
dp = [False]*1001

def go(x):
    if x>1000:
        return
    dp[x] = True
    go(x*2)
    go(x*3)
    go(x*5)

go(1)
print(dp[:15])
count = 0
for i in range(1, 1001):
    if dp[i] == True:
        count += 1
        print(i)
    if count == n:
        print(i)
        break