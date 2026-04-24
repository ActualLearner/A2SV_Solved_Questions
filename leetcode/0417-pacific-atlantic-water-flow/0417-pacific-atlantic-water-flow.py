class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        ans = []

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        
        def dfs(i, j, path):
            nonlocal visited
            nonlocal directions
            nonlocal rows
            nonlocal cols

            if all(path) or (i, j) in visited:
                return
            
            visited.add((i, j))

            for d in directions:
                u, v = i + d[0], j + d[1]

                if u < 0 or v < 0:
                    path[0] = True
                if u == rows or v == cols:
                    path[1] = True
                
                if all(path):
                    return path
                elif 0 <= u < rows and 0 <= v < cols and heights[u][v] <= heights[i][j]:
                    dfs(u, v, path)
            
            return path

        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if all(dfs(i, j, [False, False])):
                    ans.append([i, j])
                
                visited.clear()
        
        return ans
