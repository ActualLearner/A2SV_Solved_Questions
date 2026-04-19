class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = []

        for i in range(N):
            num = abs(nums[i])
            idx = num - 1

            if nums[idx] < 0:
                ans.append(idx + 1)
                continue
            
            nums[idx] = -nums[idx]
        
        for i in range(N):
            if nums[i] > 0:
                ans.append(i + 1)
        
        return ans