class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_ = 0
        left = right = 0
        zero_idx = 0
        has_zero = False

        while left < n and right < n:
            right = left
            seen = False

            if nums[left] == 0:
                zero_idx = left
                has_zero = True
                seen = True

            while right + 1 < n and (nums[right + 1] == 1 or not seen):
                right += 1

                if nums[right] != 1:
                    zero_idx = right
                    seen = True
                    has_zero = True
            
            window = right - left + (0 if seen else 1)
            max_ = max(max_, window)

            if zero_idx < left:
                break
            elif zero_idx == left:
                left += 1
            else:
                left = zero_idx + 1

        return max_ + (0 if has_zero else -1)