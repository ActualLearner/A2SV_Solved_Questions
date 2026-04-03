class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def feasible(cap):
            nonlocal weights
            nonlocal days
            d = days
            curr = 0

            for num in weights:
                if curr + num > cap:
                    curr = num
                    d -= 1
                else:
                    curr += num
            
            if curr > 0:
                d -= 1

            return d >= 0

        low, high = max(weights), sum(weights)
        while low < high:
            mid = (low + high) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        
        return high