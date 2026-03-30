class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n - 2):
            if not nums[i]:
                ans += 1

                nums[i] = 1
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]

        if not nums[-1] or not nums[-2]:
            return -1

        return ans 
