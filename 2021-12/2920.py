a = list(map(int, input().split()))

ascending = True
descending = True

for i in range(7):
    if a[i] > a[i+1]:
        ascending = False
    elif a[i] < a[i+1]:
        descending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")
