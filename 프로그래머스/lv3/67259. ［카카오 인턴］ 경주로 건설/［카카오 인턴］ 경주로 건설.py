from collections import deque

def solution(board):
    answer = 0
    n = len(board)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def bfs(x,y,direction):
        cost = [[1e9 for _ in range(n)] for _ in range(n)]
        cost[0][0] = 0
        q = deque([[x,y,direction,0]])
        while q:
            x, y, d, c = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
                    if d == i:
                        new_cost = c + 100
                    else:
                        new_cost = c + 600
                    if new_cost <= cost[nx][ny]:
                        cost[nx][ny] = new_cost
                        q.append([nx, ny, i, new_cost])
        return cost[-1][-1]
    return min(bfs(0,0,1), bfs(0,0,3))