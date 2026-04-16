def merge(left, right):
        global ans

        if not left or not right:
            return False

        merged = left + right
        if left[-1] < right[0]:
            pass
        elif right[-1] < left[0]:
            merged = right + left
            ans += 1
        else:
            return False
        
        return merged


    def merge_sort(arr):
        if len(arr) == 1:
            return arr

        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])

        return merge(left, right)

    res = merge_sort(nums)
    print(ans if res else -1)