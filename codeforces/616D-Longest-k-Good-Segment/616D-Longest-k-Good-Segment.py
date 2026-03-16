import sys
data = list(map(int, sys.stdin.read().split()))
n, k = data[0], data[1]
nums = data[2:n+2]

left = 0
count = 1
max_ = 1
max_left = 0
hashmap = {nums[left]: 1}

for right in range(1, n):
    count += 1
    hashmap[nums[right]] = hashmap.get(nums[right], 0) + 1

    while left < right and len(hashmap.keys()) > k:
        count -= 1
        hashmap[nums[left]] = hashmap.get(nums[left], 0) - 1
        if hashmap[nums[left]] <= 0:
            del hashmap[nums[left]]

        left += 1

    if count > max_ and len(hashmap.keys()) <= k:
        max_ = count
        max_left = left

if count > max_ and len(hashmap.keys()) <= k:
    max_ = count
    max_left = left

print(max_left + 1, max_left + max_)