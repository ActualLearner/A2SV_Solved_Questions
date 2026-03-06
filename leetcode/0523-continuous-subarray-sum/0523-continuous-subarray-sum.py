class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        hashmap = {}
        total = 0

        for i in range(N):
            prefix = total + nums[i]
            total += nums[i]
            curr = prefix % k

            if curr == 0 and i > 0:
                return True
            elif curr not in hashmap:
                hashmap[curr] = i
            elif i - hashmap[curr] >= 2:
                return True

        return False