number = input()

count = [0]*10
for n in number:
    count[int(n)] += 1

for i in range(9, -1, -1):
    if count[i] != 0:
        print(str(i)*count[i], end='')