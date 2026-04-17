class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()
        def feasible(d):
            start = -1e100
            count = 0

            for p in position:
                if p - start >= d:
                    start = p
                    count += 1
            
            return count >= m
                
        low, high = 1, position[-1]

        while low < high:
            mid = (low + high) // 2
            if feasible(mid):
                low = mid + 1
            else:
                high = mid
        
        return low - 1