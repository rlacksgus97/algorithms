num = input()
ans = int(num[0])

for i in range(1, len(num)):
    if ans != 0 and int(num[i]) != 0:
        ans *= int(num[i])
    else:
        ans += int(num[i])

print(ans)
