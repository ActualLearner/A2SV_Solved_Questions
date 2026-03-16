import sys
data = list(map(int, sys.stdin.read().split()))
n, k = data[0], data[1]
nums = data[2:n+2]

left = 0
max_ = 1
max_left = 0
hashmap = {nums[left]: 1}

for right in range(1, n):
    hashmap[nums[right]] = hashmap.get(nums[right], 0) + 1

    while left < right and len(hashmap) > k:
        hashmap[nums[left]] = hashmap.get(nums[left], 0) - 1
        if hashmap[nums[left]] <= 0:
            del hashmap[nums[left]]

        left += 1

    if right - left + 1 > max_ and len(hashmap) <= k:
        max_ = right - left + 1
        max_left = left

if n - left > max_ and len(hashmap) <= k:
    max_ = n - left
    max_left = left

print(max_left + 1, max_left + max_)