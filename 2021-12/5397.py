t = int(input())

for _ in range(t):
    password = input()

    left = []
    right = []
    for a in password:
        if a == '<':
            if left:
                right.append(left.pop())
        elif a == '>':
            if right:
                left.append(right.pop())
        elif a == '-':
            if left:
                left.pop()
        else:
            left.append(a)

    print(''.join(left)+''.join(reversed(right)))