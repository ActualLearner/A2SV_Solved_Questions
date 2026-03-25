class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        cols = set()
        posDiag = set()
        negDiag = set()

        path = [["."] * (n) for _ in range(n)]

        def backtrack(r):
            if r == n:
                results.append(["".join(row) for row in path])
                return

            for c in range(n):

                if c in cols or r - c in negDiag or r + c in posDiag:
                    continue

                path[r][c] = "Q"
                cols.add(c)
                negDiag.add(r - c)
                posDiag.add(r + c)

                backtrack(r + 1)

                cols.remove(c)
                negDiag.remove(r - c)
                posDiag.remove(r + c)
                path[r][c] = "."
        
        backtrack(0)
        return results