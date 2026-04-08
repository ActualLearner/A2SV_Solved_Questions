class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        ans = 0

        i = 0
        while i < len(nums) and miss <= n:
            if nums[i] <= miss:
                miss += nums[i]
                i += 1
            elif nums[i] > miss:
                ans += 1
                miss += miss
            
        while miss <= n:
            miss += miss
            ans += 1
        
        return ans
