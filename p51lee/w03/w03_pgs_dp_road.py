def solution(m, n, puddles):
    field = [[-1]*n for _ in range(m)] # field[x][y]
    
    for i in range(m):
        field[i][0] = 1
        
    for j in range(n):
        field[0][j] = 1
    
    for puddle in puddles:
        puddle_x = puddle[0]
        puddle_y = puddle[1]
        if puddle_y == 1:
            for i in range(puddle_x-1, m):
                field[i][0] = 0
        elif puddle_x == 1:
            for j in range(puddle_y-1, n):
                field[0][j] = 0
        else:
            field[puddle_x - 1][puddle_y - 1] = 0
    
    for walk in range(1, min(m, n)):
        for walk_right in range(walk, m):
            if field[walk_right][walk] == 0:
                continue
            else:
                field[walk_right][walk] = (field[walk_right-1][walk] + field[walk_right][walk-1]) % 1000000007
        
        for walk_down in range(walk+1, n):
            if field[walk][walk_down] == 0:
                continue
            else:
                field[walk][walk_down] = (field[walk-1][walk_down] + field[walk][walk_down-1]) % 1000000007 
        
    return field[m-1][n-1]%1000000007
