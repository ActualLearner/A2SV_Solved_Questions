N, K = list(map(int, input().split()))
nums = list(map(int, input().split()))

dp = [0] * N
for i in range(1, N):
  dp[i] = dp[i - 1] + abs(nums[i] - nums[i - 1])
  
  for j in range(max(0, i - K), i):
      dp[i] = min(dp[i], dp[j] + abs(nums[i] - nums[j]))

print(dp[-1])