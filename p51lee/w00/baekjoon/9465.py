import sys

board_list = []
for _ in range(int(sys.stdin.readline())):
    length = int(sys.stdin.readline())
    board = []
    board.append(list(map(int, sys.stdin.readline().split())))
    board.append(list(map(int, sys.stdin.readline().split())))
    board_list.append((length, board))

ans = []
for length, board in board_list:
    if length > 1:
        board[1][1] += board[0][0]
        board[0][1] += board[1][0]
        for i in range(2, length):
            board[1][i] += max(board[0][i-1], board[0][i-2])
            board[0][i] += max(board[1][i-1], board[1][i-2])
    ans.append(max(board[0][-1], board[1][-1]))
print(*ans, sep="\n")
