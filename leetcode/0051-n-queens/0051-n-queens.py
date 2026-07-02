class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["." for _ in range(n)] for _ in range(n)]
        cols = [0] * n
        posDiag = [False] * (2*n - 1)
        negDiag = [False] * (2*n - 1)

        def backtrack(i, board):
            if i == n:
                ans.append(["".join(x) for x in board])
                return
            
            for j in range(n):
                if cols[j] or posDiag[i + j] or negDiag[i - j]:
                    continue
                
                cols[j] = True
                posDiag[i + j] = True
                negDiag[i - j] = True
                board[i][j] = "Q"

                backtrack(i + 1, board)

                cols[j] = False
                posDiag[i + j] = False
                negDiag[i - j] = False
                board[i][j] = "."
        
        backtrack(0, board)
        return ans