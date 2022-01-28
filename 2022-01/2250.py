#Tree

class Node:
    def __init__(self, data, left, right):
        self.parent = -1
        self.data = data
        self.left = left
        self.right = right

def traverse(node, level):
    global deepest, order
    deepest = max(deepest, level)
    if node.left != -1:
        traverse(tree[node.left], level+1)
    level_l[level] = min(level_l[level], order)
    level_r[level] = max(level_r[level], order)
    order += 1
    if node.right != -1:
        traverse(tree[node.right], level+1)

n = int(input())
tree = {}
root = 0
deepest = 0
order = 1
level_l = [n for _ in range(n+1)]
level_r = [0 for _ in range(n+1)]

for i in range(1, n+1):
    tree[i] = Node(i, -1, -1)

for _ in range(n):
    data, left, right = map(int, input().split())
    tree[data].left = left
    tree[data].right = right
    if left != -1:
        tree[left].parent = data
    if right != -1:
        tree[right].parent = data

for i in range(1, n+1):
    if tree[i].parent == -1:
        root = i
        break

traverse(tree[root], 1)

result_level = 1
result_width = 1
for i in range(1, deepest+1):
    width = level_r[i]-level_l[i]+1
    if result_width < width:
        result_level = i
        result_width = width

print(result_level, result_width)