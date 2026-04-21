class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = []

        for i in range(N):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                ans.append(abs(nums[i]))
            else:
                nums[idx] = -nums[idx]
        
        return ans