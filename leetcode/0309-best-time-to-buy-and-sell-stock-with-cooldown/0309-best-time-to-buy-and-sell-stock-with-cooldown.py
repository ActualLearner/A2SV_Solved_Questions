class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [[0] * (N + 1), [float("-inf")] * (N + 1), [float("-inf")] * (N + 1)]
        dp[2][0] = 0
        
        for i in range(N):
            dp[0][i + 1] = max(dp[0][i], dp[1][i] + prices[i])
            dp[2][i + 1] = dp[0][i]
            dp[1][i + 1] = max(dp[1][i], dp[2][i] - prices[i])
        
        return max(dp[0][-1], dp[2][-1])
