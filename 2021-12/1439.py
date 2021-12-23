s = input()

count_zero = 0
count_one = 0
if s[0] == '0':
    count_zero += 1
else:
    count_one += 1

for i in range(len(s)-1):
    if s[i] == '0' and s[i+1] == '1':
        count_one += 1
    elif s[i] == '1' and s[i+1] == '0':
        count_zero += 1

print(min(count_zero, count_one))