class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_ = 10**18
        total = 0
        
        for num in nums:
            total += num
            min_ = min(total, min_)
        
        return abs(min_) + 1 if min_ < 0 else 1