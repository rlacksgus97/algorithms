n = int(input())
k = int(input())
apple = []
for _ in range(k):
    apple.append(tuple(map(int, input().split())))
l = int(input())
direction = []
for _ in range(l):
    direction.append(tuple(input().split()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d = 0

def turn(direction):
    global d
    if direction == 'L':
        if d == 0:
            d = 3
        else:
            d -= 1
    else:
        if d == 3:
            d = 0
        else:
            d += 1

snake = [(1,1)]
tick = 0
x, c = direction.pop(0)
while True:
    if tick == int(x):
        turn(c)
        if direction:
            x, c = direction.pop(0)
    tick += 1
    head_x = snake[0][0] + dx[d]
    head_y = snake[0][1] + dy[d]
    if head_x > n or head_x < 1 or head_y > n or head_y < 1:
        break
    if (head_x, head_y) in snake:
        break
    snake.insert(0, (head_x, head_y))
    if (head_x, head_y) in apple:
        apple.remove((head_x, head_y))
    else:
        snake.pop()
        
print(tick)