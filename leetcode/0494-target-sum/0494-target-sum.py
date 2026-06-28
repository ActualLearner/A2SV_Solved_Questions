class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        dp = [defaultdict(int) for _ in range(N + 1)]
        dp[0][0] = 1

        for i in range(N):
            for cur_sum, count in dp[i].items():
                dp[i + 1][cur_sum + nums[i]] += count
                dp[i + 1][cur_sum - nums[i]] += count
        
        return dp[-1][target]