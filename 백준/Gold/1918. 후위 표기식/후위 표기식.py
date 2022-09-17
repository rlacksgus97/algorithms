expression = input()
priority = {'+': 0, '-': 0, '*': 1, '/': 1, '(': -1}


def postfix(exp, stack, result):
    idx = 0
    while idx < len(exp):
        e = exp[idx]
        if 'A' <= e <= 'Z':
            result += e
        elif e in ['*', '/', '+', '-']:
            while stack and priority[stack[-1]] >= priority[e]:
                result += stack.pop()
            stack.append(e)
        elif e == '(':
            stack.append(e)
        elif e == ')':
            while stack:
                op = stack.pop()
                if op == '(':
                    break
                result += op
        idx += 1
    while stack:
        result += stack.pop()
    return result


print(postfix(expression, [], ''))
