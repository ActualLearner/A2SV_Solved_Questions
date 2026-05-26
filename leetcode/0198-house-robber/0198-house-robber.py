class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[0]

        if n == 1:
            return prev

        curr = max(nums[0], nums[1])

        for i in range(2, n):
            temp = prev
            prev = curr
            curr = max(curr, temp + nums[i])
        
        return curr