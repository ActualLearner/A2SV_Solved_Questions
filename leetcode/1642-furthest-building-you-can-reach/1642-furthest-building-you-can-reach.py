class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        costs = []

        for i in range(1, n):
            diff = heights[i] - heights[i - 1]
            if diff <= 0:
                continue
            
            if diff <= bricks:
                bricks -= diff
                heappush(costs, -diff)
            elif ladders > 0:
                ladders -= 1
                if costs and -costs[0] > diff:
                    bricks += -(heappop(costs))
                    bricks -= diff
                    heappush(costs, -diff)
            else:
                return i - 1
        
        return n - 1