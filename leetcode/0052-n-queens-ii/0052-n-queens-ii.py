class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        cols = [False for _ in range(n)]
        posDiag = [False for _ in range(2*n)]
        negDiag = [False for _ in range(2*n)]

        def place(r):
            nonlocal ans
            nonlocal cols
            nonlocal posDiag
            nonlocal negDiag

            if r == n:
                ans += (1 if cols.count(True) == n else 0)
                return
            
            for idx in range(n):
                if cols[idx] or posDiag[r + idx] or negDiag[r - idx]:
                    continue
                    
                cols[idx] = True
                posDiag[r + idx] = True
                negDiag[r - idx] = True
                
                place(r + 1)
                cols[idx] = False
                posDiag[r + idx] = False
                negDiag[r - idx] = False

        place(0)
        return ans