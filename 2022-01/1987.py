#가장 긴 이동 거리는 bfs로 푸는게 나을듯?

r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(input()))

answer = 1
def rec_func(x, y, count):
    global answer
    for d in [(-1,0),(0,1),(1,0),(0,-1)]:
        nx = x + d[0]
        ny = y + d[1]
        if 0<=nx<r and 0<=ny<c and alphabet[ord(board[nx][ny])-ord('A')] == 0:
            alphabet[ord(board[nx][ny])-ord('A')] = 1
            rec_func(nx, ny, count+1)
            alphabet[ord(board[nx][ny])-ord('A')] = 0
    answer = max(answer, count)

alphabet = [0 for _ in range(26)]
alphabet[ord(board[0][0])-ord('A')] = 1
rec_func(0, 0, 1)
print(answer)
