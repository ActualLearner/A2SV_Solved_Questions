class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        seen = {}
        ans = 0

        total = 0
        for num in nums:
            total += num
            diff = total - goal

            if diff == 0:
                ans += 1
            
            if diff in seen:
                ans += seen[diff]
            
            seen[total] = seen.get(total, 0) + 1

        return ans