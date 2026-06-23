class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        dp = [[0] * (N + 1), [float("-inf") for _ in range(N + 1)]]

        for i in range(N):
            dp[1][i + 1] = max(dp[1][i], dp[0][i] - prices[i])
            dp[0][i + 1] = max(dp[0][i], dp[1][i] + prices[i] - fee)
        
        return max(dp[0][-1], dp[1][-1])