class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def quickselect(left, right):
            lt, idx, gt = left, left, right
            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]

            while idx <= gt:
                if nums[idx] < pivot:
                    nums[lt], nums[idx] = nums[idx], nums[lt]
                    lt += 1
                    idx += 1
                elif nums[idx] > pivot:
                    nums[gt], nums[idx] = nums[idx], nums[gt]
                    gt -= 1
                else:
                    idx += 1
            
            if k < lt:
                return quickselect(left, lt - 1)
            elif k > gt:
                return quickselect(gt + 1, right)
            else:
                return nums[k]
        
        return quickselect(0, len(nums) - 1)