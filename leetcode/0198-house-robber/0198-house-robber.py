class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = prev2 = 0

        for num in nums:
            curr = max(prev1 + num, prev2)
            prev1 = prev2
            prev2 = curr
        
        return prev2