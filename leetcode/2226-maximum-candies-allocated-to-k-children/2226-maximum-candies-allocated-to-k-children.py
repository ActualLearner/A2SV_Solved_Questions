class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def feasible(target):
            count = 0
            for num in candies:
                count += (num // target)
                if count >= k:
                    return True
            
            return False

        if k > sum(candies):
            return 0
        
        low, high = 1, max(candies) + 1
        while low < high:
            mid = (low + high) // 2
            if not feasible(mid):
                high = mid
            else:
                low = mid + 1
        
        return low - 1