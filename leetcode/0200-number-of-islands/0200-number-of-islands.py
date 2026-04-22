class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols:
                return
            if grid[i][j] == '0':
                return
            if (i, j) in visited:
                return
            
            visited.add((i, j))
            
            for di, dj in directions:
                dfs(i + di, j + dj)
        
        count = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    count += 1
                    dfs(i, j)
        
        return count