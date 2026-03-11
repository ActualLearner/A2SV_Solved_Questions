from collections import Counter
n, m = list(map(int, input().split()))
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

counter = Counter(nums1)

ans = 0
for num in nums2:
    ans += counter[num]

print(ans)