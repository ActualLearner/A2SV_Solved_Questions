class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low, high = 0, len(nums) - 1
        if nums[low] < nums[high]:
            return nums[low]

        while low < high:
            mid = (low + high) // 2
            if nums[mid] < nums[0]:
                high = mid
            else:
                low = mid + 1

        return nums[low]