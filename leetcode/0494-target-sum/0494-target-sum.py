class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        cache = {}

        def dfs(val, i):
            if i == N:
                return 1 if val == target else 0
            
            if (val + nums[i], i + 1) not in cache:
                cache[(val + nums[i], i + 1)] = dfs(val + nums[i], i + 1)

            if (val - nums[i], i + 1) not in cache:
                cache[(val - nums[i], i + 1)] = dfs(val - nums[i], i + 1)

            left = cache[(val + nums[i], i + 1)]
            right = cache[(val - nums[i], i + 1)]
            return left + right
        
        return dfs(0, 0)
