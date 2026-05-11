class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        def merge(left, right):
            i = 0
            for idx in left:
                while i < len(right) and nums[idx] > nums[right[i]]:
                    i += 1
                ans[idx] += i
            
            merged = []
            l, r = 0, 0
            while l < len(left) and r < len(right):
                if nums[left[l]] <= nums[right[r]]:
                    merged.append(left[l])
                    l += 1
                else:
                    merged.append(right[r])
                    r += 1
            
            merged.extend(left[l:])
            merged.extend(right[r:])
            return merged

        
        def merge_sort(nums):
            if len(nums) == 1:
                return nums

            left = merge_sort(nums[:len(nums) // 2])
            right = merge_sort(nums[len(nums) // 2:])

            return merge(left, right)
        
        merge_sort([i for i in range(len(nums))])
        return ans