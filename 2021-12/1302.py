n = int(input())

board = {}
for _ in range(n):
    book = input()
    if book in board:
        board[book] += 1
    else:
        board[book] = 1

top = max(board.values())
answer = []

for book, count in board.items():
    if count == top:
        answer.append(book)

print(sorted(answer)[0])

#fail