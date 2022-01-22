from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
score = 0

def find_group(a, b, visited):
    normal = [(a,b)]
    rainbow = []
    q = deque([(a, b)])
    visited[a][b] = True
    while q:
        x, y = q.popleft()
        for d in [(-1,0), (0,1), (1,0), (0,-1)]:
            nx = x + d[0]
            ny = y + d[1]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if board[nx][ny] == board[a][b]:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    normal.append((nx,ny))
                if board[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    rainbow.append((nx,ny))

    for x, y in rainbow:
        visited[x][y] = False

    return [len(normal)+len(rainbow), len(rainbow), normal+rainbow]

#블록 그룹을 찾는 함수
#0. dfs/bfs로 그룹핑
#1. 크기가 가장 큰 것
#2. 무지개 블록이 가장 많은 것
#3. 기준 블록의 행이 가장 큰 것
#4. 기준 블록의 열이 가장 큰 것
#1,2,3,4 순서로 info 리스트에 저장 후 sort(find_group())
def find_largest_group():
    visited = [[False for _ in range(n)] for _ in range(n)]
    candidate = []
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 and visited[i][j] == False:
                group_info = find_group(i,j, visited)
                if group_info[0] >= 2:
                    candidate.append(group_info)

    candidate.sort(reverse=True)
    
    return candidate[0]

#find_largest_group에서 선택한 블록 그룹 제거, 점수 계산
def remove_and_count(group):
    global score
    for x,y in group:
        board[x][y] = -2
    score += group[0]**2

#중력 작용
def gravity(board):
    pass

#반시계로 90도 회전
def rotate(board):
    pass

while True:
    group = find_largest_group()
    if group == []:
        break
    else:
        remove_and_count(group)
    gravity(board)
    rotate(board)
    gravity(board)

print(score)