import numpy as np

def pick(l, d, x, y, board):
    if d == 0:
        for i in range(y-1, y-1+l):
            board[x-1][i] = 1
    else:
        for i in range(x-1, x-1+l):
            board[i][y-1] = 1

    return board

board_height, board_width = map(int, input().split())

board = np.zeros((board_height, board_width), dtype=int)

n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    board = pick(l, d, x, y, board)

for i in range(board_height):
    for j in range(board_width):
        print(board[i][j], end = ' ')
    print()
