class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for _ in range(n)]

        for _ in range(m - 1):
            new_dp = [0 for _ in range(n)]
            new_dp[0] = 1

            for i in range(1, n):
                new_dp[i] += dp[i] + new_dp[i - 1]
            
            dp = new_dp
        
        return dp[-1]