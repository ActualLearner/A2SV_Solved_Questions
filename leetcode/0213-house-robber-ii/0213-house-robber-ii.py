class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        
        ans = 0

        prev = prev2 = 0
        for i in range(n - 1):
            curr = max(prev, prev2 + nums[i])
            prev2 = prev
            prev = curr

        ans = prev

        prev = prev2 = 0
        for i in range(1, n):
            curr = max(prev, prev2 + nums[i])
            prev2 = prev
            prev = curr
        
        return max(prev, ans)