class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        prefix = [0 for _ in range(n + 1)]

        for req in requests:
            prefix[req[0]] += 1
            prefix[req[1] + 1] -= 1
        
        for i in range(1, n + 1):
            prefix[i] += prefix[i - 1]

        prefix.sort(reverse=True)
        nums.sort(reverse=True)
        ans = 0

        for i in range(n):
            ans += (nums[i] * prefix[i])
        
        return ans % (10**9 + 7)