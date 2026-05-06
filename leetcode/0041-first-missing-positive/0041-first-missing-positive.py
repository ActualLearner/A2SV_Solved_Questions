class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
        
            idx = nums[i] - 1
            while idx != i and nums[i] > 0 and nums[i] <= n:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx = nums[i] - 1
                
                if 0 <= idx < n and nums[idx] == nums[i]:
                    break

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
            
        return n + 1