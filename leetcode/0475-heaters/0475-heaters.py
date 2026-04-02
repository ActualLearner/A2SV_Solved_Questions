class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        max_ = 0
        
        for h in houses:
            idx = bisect.bisect_left(heaters, h)
            
            dist_right = abs(heaters[idx] - h) if 0 <= idx < len(heaters) else float("inf")
            dist_left = abs(heaters[idx - 1] - h) if 0 <= idx - 1 < len(heaters) else float("inf") 

            max_ = max(max_, min(dist_right, dist_left))
        
        return max_