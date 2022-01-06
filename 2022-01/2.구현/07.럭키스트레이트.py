point = input()

left = 0
for i in range(len(point)//2):
    left += int(point[i])

right = 0
for i in range(len(point)//2, len(point)):
    right += int(point[i])

if left == right:
    print("LUCKY")
else:
    print("READY")