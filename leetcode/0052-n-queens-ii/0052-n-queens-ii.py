class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        cols = [False] * n
        posDiag = [False] * (2*n - 1)
        negDiag = [False] * (2*n - 1)

        def backtrack(i):
            nonlocal ans

            if i == n:
                return 1
            
            count = 0
            
            for j in range(n):
                if cols[j] or posDiag[i + j] or negDiag[i - j]:
                    continue
                
                cols[j] = True
                posDiag[i + j] = True
                negDiag[i - j] = True

                count += backtrack(i + 1)

                cols[j] = False
                posDiag[i + j] = False
                negDiag[i - j] = False
            
            return count
        
        return backtrack(0)