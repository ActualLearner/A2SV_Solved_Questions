class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        prefix = []
        total = 0
        for num in nums:
            total += num
            prefix.append(total)

        min_ = 0
        ans = prefix[0]

        for i in range(1, len(prefix)):
            max_ = max(prefix[i], prefix[i] - prefix[min_])
            ans = max(ans, max_)

            if prefix[i] < prefix[min_]:
                min_ = i

        
        return ans

