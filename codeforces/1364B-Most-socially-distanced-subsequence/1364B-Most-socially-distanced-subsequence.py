import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    N = int(input())
    nums = list(map(int, input().split()))

    ans = [nums[0]]
    for i in range(1, N - 1):
        increasing = nums[i - 1] < nums[i] < nums[i + 1]
        decreasing = nums[i - 1] > nums[i] > nums[i + 1]

        if increasing or decreasing:
            continue
        else:
            ans.append(nums[i])

    ans.append(nums[-1])
    print(len(ans))
    print(*ans)