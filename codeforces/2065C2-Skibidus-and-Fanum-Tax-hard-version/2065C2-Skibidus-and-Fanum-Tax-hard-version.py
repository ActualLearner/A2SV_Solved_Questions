import sys
input = sys.stdin.readline

def search(arr, target, lesser):
    low, high = 0, len(arr)

    while low < high:
        mid = (low + high) // 2
        if arr[mid] - target >= lesser:
            high = mid
        else:
            low = mid + 1
    
    return arr[low] - target if low != len(arr) else float("-inf")


t = int(input())
out = []

for _ in range(t):
    n, m = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()

    nums[0] = min(nums[0], b[-1] - nums[0], b[0] - nums[0]) 

    for i in range(1, n):
        substitute = search(b, nums[i], nums[i - 1])

        if nums[i-1] <= nums[i] and nums[i - 1] <= substitute:
            nums[i] = min(nums[i], substitute)
        elif nums[i - 1] <= substitute:
            nums[i] = substitute
        
        if nums[i - 1] > nums[i]:
            break

    else:
        out.append("YES")
        continue

    out.append("NO")

sys.stdout.write("\n".join(out))