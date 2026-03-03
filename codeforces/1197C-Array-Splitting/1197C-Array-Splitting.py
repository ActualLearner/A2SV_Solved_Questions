import sys
data = list(map(int, sys.stdin.read().split()))
n, k = data[0], data[1]
nums = data[2:]

if k == 1:
    print(nums[-1] - nums[0])
else:
    gaps = []
    for i in range(1, n):
        gaps.append(nums[i] - nums[i-1])

    gaps.sort()
    print(sum(gaps[:len(gaps)-(k-1)]))