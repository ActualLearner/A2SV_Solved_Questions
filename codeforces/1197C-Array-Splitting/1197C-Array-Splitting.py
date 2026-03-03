import sys
data = list(map(int, sys.stdin.read().split()))
n = data[0]
k = data[1]
nums = data[2:]

if n == k:
    sys.stdout.write("0")
elif k == 1:
    sys.stdout.write(str(nums[-1] - nums[0]))
else:
    hashmap = {}
    for i in range(1, n):
        gap = nums[i] - nums[i - 1]
        hashmap[i] = gap

    gaps = [i for i in range(1, len(nums))]
    gaps.sort(reverse=True, key=lambda x: hashmap[x])

    gaps = gaps[:k-1]

    cost = 0
    for i in range(len(gaps)):
        if i == 0:
            cost += (nums[-1] - nums[gaps[i]])
        else:
            cost += (nums[gaps[i - 1] - 1] - nums[gaps[i]])

    cost += nums[gaps[-1] - 1] - nums[0]

    sys.stdout.write(str(cost))