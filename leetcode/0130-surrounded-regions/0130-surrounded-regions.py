class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        rows, cols = len(board), len(board[0])
        
        def dfs(i, j):
            nonlocal visited
            if i < 0 or j < 0 or i == rows or j == cols:
                return
            elif (i, j) in visited or board[i][j] == "X":
                return
            
            visited.add((i, j))
            board[i][j] = "T"
            
            for d in directions:
                dfs(i + d[0], j + d[1])
        
        for i in range(rows):
            for j in range(cols):
                if i in [0, rows - 1] or j in [0, cols - 1]:
                    if board[i][j] == "O":
                        dfs(i, j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        