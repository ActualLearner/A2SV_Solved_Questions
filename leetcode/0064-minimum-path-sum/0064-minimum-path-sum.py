class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dist = defaultdict(lambda: float("inf"))
        source = (0, 0)
        dist[source] = grid[0][0]
        min_heap = [(dist[source], source)]

        while min_heap:
            curr = heappop(min_heap)
            i, j = curr[1]
            
            if i + 1 < n:
                nei = (i + 1, j)
                if dist[nei] > curr[0] + grid[i + 1][j]:
                    dist[nei] = curr[0] + grid[i + 1][j]
                    heappush(min_heap, (dist[nei], nei))

            if j + 1 < m:
                nei = (i, j + 1)
                if dist[nei] > curr[0] + grid[i][j + 1]:
                    dist[nei] = curr[0] + grid[i][j + 1]  
                    heappush(min_heap, (dist[nei], nei))
        
        return dist[(n - 1, m - 1)]