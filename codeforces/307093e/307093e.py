n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))

window = {}
left = 0
ans = 0

for right in range(n):
    window[nums[right]] = window.get(nums[right], 0) + 1

    while len(window) > k:
        window[nums[left]] = window.get(nums[left], 0) - 1

        if window.get(nums[left]) == 0:
            del window[nums[left]]

        left += 1

    ans += right - left + 1

print(ans)