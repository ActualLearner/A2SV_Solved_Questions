N = int(input())
dp = [[0] * (N + 1), [0] * (N + 1), [0] * (N + 1)]

for i in range(N):
  a, b, c = list(map(int, input().split()))
  dp[0][i + 1] = a + max(dp[1][i], dp[2][i])
  dp[1][i + 1] = b + max(dp[0][i], dp[2][i])
  dp[2][i + 1] = c + max(dp[0][i], dp[1][i])
  
print(max(dp[0][-1], dp[1][-1], dp[2][-1]))