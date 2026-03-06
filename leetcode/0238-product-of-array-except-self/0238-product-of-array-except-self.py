class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        
        for i in range(len(nums) - 1):
            ans.append(ans[-1] * nums[i])
        
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= curr
            curr *= nums[i]
        
        return ans