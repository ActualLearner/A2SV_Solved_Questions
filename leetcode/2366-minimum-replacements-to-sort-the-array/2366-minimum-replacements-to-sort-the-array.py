class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[-1]
        ans = 0

        for i in range(n - 2, -1, -1):
            if nums[i] > prev:
                count = nums[i] // prev
                if nums[i] % prev:
                    count += 1
                
                prev = nums[i] // count
                ans += (count - 1)
            else:
                prev = nums[i]
        
        return ans
