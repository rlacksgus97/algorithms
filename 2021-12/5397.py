t = int(input())

for _ in range(t):
    a = input()
    left = []
    right = []

    for x in a:
        if x == '<':
            if left != []:
                right.append(left.pop())
        elif x == '>':
            if right != []:
                left.append(right.pop())
        elif x == '-':
            if left != []:
                left.pop()
        else:
            left.append(x)
    left.extend(reversed(right))
    print(''.join(left))

#fail