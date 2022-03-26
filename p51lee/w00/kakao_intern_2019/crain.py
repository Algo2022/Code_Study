def transpose(board):
    n = len(board)
    trans = []
    for j in range(n):
        temp = []
        for i in range(n):
            if board[i][j]:
                temp.append(board[i][j])
        trans.append(temp[::-1])
    return trans

def solution(board, moves):
    answer = 0
    stack = []
    boardT = transpose(board)
    for move in moves:
        move -= 1
        if boardT[move]:
            new = boardT[move].pop()
            if stack and new == stack[-1]:
                stack.pop()
                answer += 2
            else:
                stack.append(new)
    return answer

