class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac_visited = set()
        atl_visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j, visited):
            visited.add((i, j))

            for d in directions:
                u, v = i + d[0], j + d[1]
                if 0 <= u < rows and 0 <= v < cols and (u, v) not in visited and heights[u][v] >= heights[i][j]:
                    dfs(u, v, visited)

        for c in range(cols):
            dfs(0, c, pac_visited)
            dfs(rows - 1, c, atl_visited)
        
        for r in range(rows):
            dfs(r, 0, pac_visited)
            dfs(r, cols - 1, atl_visited)
        
        return list(pac_visited & atl_visited)