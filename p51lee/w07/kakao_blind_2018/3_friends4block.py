class Board():
    def __init__(self, m, n, board):
        self.rows = m
        self.cols = n
        self.board = []
        self.ans = 0
        string = "".join(board)
        for j in range(n):
            acc = []
            for i in range(m):
                acc.append(string[n*i + j])
            self.board.append(acc)
        
    
    def __getitem__(self, index):
        i, j = index
        return self.board[j][i]
    
    def __setitem__(self, index, value):
        i, j = index
        self.board[j][i] = value
    
    def square(self, i, j):
        same = self[i,j] == self[i+1,j] == self[i,j+1] == self[i+1,j+1]
        null = self[i,j] == "X"
        if same and not null:
            return True
        else:
            return False
        
    def delete4(self, victim):
        i, j = victim
        if self[i,j] != "X":
            self.ans += 1
            self[i,j] = "X"
        if self[i,j+1] != "X":
            self.ans += 1
            self[i,j+1] = "X"
        if self[i+1,j] != "X":
            self.ans += 1
            self[i+1,j] = "X"
        if self[i+1,j+1] != "X":
            self.ans += 1
            self[i+1,j+1] = "X"
        
    def delete(self):
        deathNote = []
        diff = False
        for i in range(self.rows-1):
            for j in range(self.cols-1):
                if self.square(i, j):
                    deathNote.append((i,j))
        for victim in deathNote:
            self.delete4(victim) 
            diff = True
        return diff
    
    def fall(self):
        for i in range(self.cols):
            self.board[i] = list("".join(self.board[i]).replace("X", "").rjust(self.rows, "X"))
        
    def solution(self):
        while self.delete():
            self.fall()
        return self.ans
    
solution = lambda m, n, b: Board(m, n, b).solution()