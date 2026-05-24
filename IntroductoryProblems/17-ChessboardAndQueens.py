if __name__ == "__main__":
    chessBoard = []

    for i in range(8):
        chessBoard.append(list(input().strip()))
    
    res = [0]

    def isValid(pos, m, n, curr):
        # same row
        for j in range(pos[1] + 1, n):
            if (pos[0], j) in curr:
                return False
        
        for j in range(pos[1] - 1, -1, -1):
            if (pos[0], j) in curr:
                return False
            
        # same col
        for i in range(pos[0] + 1, m):
            if (i, pos[1]) in curr:
                return False
        
        for i in range(pos[0] - 1, -1, -1):
            if (i, pos[1]) in curr:
                return False
        
        # top-left to bottom-right diagonal
        for i in range(m):
            for j in range(n):
                if pos[0] - pos[1] == i - j and (i, j) in curr:
                    return False
        
        # top-right to bottom-left diagonal
        for i in range(m):
            for j in range(n):
                if pos[0] + pos[1] == i + j and (i, j) in curr:
                    return False
        
        return True
            
    def nQueens(m, n, x, curr):
        if x == m:
            if len(curr) == m:
                res[0] += 1
            return
        
        nQueens(m, n, x + 1, curr)

        for y in range(n):
            pos = (x, y)
            if pos[0] >= 0 and pos[0] < m and pos[1] >= 0 and pos[1] < n and chessBoard[pos[0]][pos[1]] == "." and isValid(pos, m, n, curr):
                curr.add(pos)
                nQueens(m, n, x + 1, curr)
                curr.remove(pos)

    
    nQueens(8, 8, 0, set())

    print(res[0])

        
            
            
            


