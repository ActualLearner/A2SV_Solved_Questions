N = int(input())
nums = list(map(int, input().split()))
dp = [0] * N

for i in range(1, N):
    if i == 1:
        dp[i] = abs(nums[i] - nums[i-1])
    else:
        dp[i] = min(dp[i-1] + abs(nums[i] - nums[i-1]), dp[i-2] + abs(nums[i] - nums[i-2]))
        
print(dp[-1])