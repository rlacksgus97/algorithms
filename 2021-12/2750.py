n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))

for i in range(n):
    min_i = i
    for j in range(i+1, n):
        if num[min_i] > num[j]:
            min_i = j
    num[i], num[min_i] = num[min_i], num[i]

for i in num:
    print(i)