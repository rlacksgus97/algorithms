num = input()
ans = int(num[0])

for i in range(1, len(num)):
    if ans <= 1 or int(num[i]) <= 1:
        ans += int(num[i])
    else:
        ans *= int(num[i])

print(ans)
