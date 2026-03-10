import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    N = int(input())
    nums = list(map(int, input().split()))

    max_diff = 0
    for i in range(N - 1):
        max_diff += abs(nums[i] - nums[i + 1])

    ans = []
    for i in range(N - 1):
        curr_diff = max_diff
        curr_diff -= abs(nums[i] - nums[i + 1])

        if i != 0:
            curr_diff -= abs(nums[i - 1] - nums[i])
            curr_diff += abs(nums[i - 1] - nums[i + 1])

        if curr_diff == max_diff:
            continue
        else:
            ans.append(nums[i])

    ans.append(nums[-1])
    print(len(ans))
    print(*ans)