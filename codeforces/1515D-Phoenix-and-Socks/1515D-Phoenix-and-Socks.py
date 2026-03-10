from collections import Counter
import sys
data = list(map(int, sys.stdin.read().split()))
t = int(data[0])
idx = 1
for _ in range(t):
    n, l, r = data[idx], data[idx+1], data[idx+2]
    idx += 3
    nums = data[idx:idx+n]
    idx += n

    nums_left = nums[:l]
    nums_right = nums[l:]

    count_left = Counter(nums_left)
    count_right = Counter(nums_right)

    for key, value in count_left.items():
        match = min(value, count_right[key])
        count_right[key] -= match
        count_left[key] -= match

    left_rem = sum(count_left.values())
    right_rem = sum(count_right.values())
    excess = abs(left_rem - right_rem) // 2
    possible_pairs = 0

    if l > r:
        possible_pairs = sum(val // 2 for val in count_left.values())
    elif r > l:
        possible_pairs = sum(val // 2 for val in count_right.values())

    ans = max(left_rem, right_rem) - min(excess, possible_pairs)

    print(ans)