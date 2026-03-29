class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = []
        
        total = 0
        for i in range(n):
            total += nums[i]
            prefix.append(total % k)
        
        seen = {0:1}
        ans = 0

        for p in prefix:
            ans += seen.get(p, 0)
            seen[p] = seen.get(p, 0) + 1
        
        return ans