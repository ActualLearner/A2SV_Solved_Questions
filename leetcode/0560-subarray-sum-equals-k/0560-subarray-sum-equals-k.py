class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        seen = {}
        total = 0
        ans = 0

        for i in range(N):
            total += nums[i]
            diff = total - k

            if diff == 0:
                ans += 1

            if diff in seen:
                ans += seen[diff]

            seen[total] = seen.get(total, 0) + 1
        
        return ans
