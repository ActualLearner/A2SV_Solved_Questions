n, s = list(map(int, input().split()))
nums = list(map(int, input().split()))

left = right = 0
window = 0
ans = 0

for right in range(n):
    window += nums[right]

    while window > s:
        window -= nums[left]
        left += 1

    ans += right - left + 1

print(ans)