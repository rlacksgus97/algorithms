n = int(input())
array = []
for _ in range(3):
    array.append(int(input()))
array.sort(reverse=True)
for i in array:
    print(i, end=' ')