class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)

        low, high = 0, n
        while low < high:
            mid = (low + high) // 2
            
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1

        return high