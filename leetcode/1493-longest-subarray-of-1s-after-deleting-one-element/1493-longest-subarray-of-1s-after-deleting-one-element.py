class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_ = 0

        window = 0
        left = 0

        for right in range(n):
            window += nums[right]

            while (right - left + 1) - window > 1:
                window -= nums[left]
                left += 1

            max_ = max(max_, right - left)
        
        return max_


