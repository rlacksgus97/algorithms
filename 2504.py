s = list(input())
stack = []
answer = 0
temp = 1
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
        temp *= 2
    elif s[i] == '[':
        stack.append(s[i])
        temp *= 3
    elif s[i] == ')':
        if not stack or stack[-1] == "[":
            answer = 0
            break
    elif s[i] == ']':
        if not stack or stack[-1] == "(":
            answer = 0
            break

print(answer)