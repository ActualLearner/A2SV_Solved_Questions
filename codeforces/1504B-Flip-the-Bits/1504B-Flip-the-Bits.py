t = int(input())

for _ in range(t):
    n = int(input())
    nums1 = list(input().strip())
    nums2 = list(input().strip())

    if nums1 == nums2:
        print("YES")
        continue
    elif n == 1:
        print("YES" if nums1 == nums2 else "NO")
        continue

    prefix = []

    total = 0
    for num in nums1:
        total += int(num)
        prefix.append(total)

    flipped = False

    for i in range(n - 1, -1, -1):
        can_flip = (prefix[i] == ((i + 1) / 2))

        curr = nums1[i]
        if flipped:
            curr = '1' if nums1[i] == '0' else '0'

        if curr != nums2[i]:
            if not can_flip:
                print("NO")
                break
            else:
                flipped = not flipped
    else:
        print("YES")