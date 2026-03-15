class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        
        prefix = []
        total = 0
        for num in nums:
            total += num
            prefix.append(total)
        
        ans = 0

        hashmap = {}
        for num in prefix:
            if num == goal:
                ans += 1
                if 0 in hashmap:
                    ans += hashmap[0]
            elif num > goal:
                target = num - goal
                if target in hashmap:
                    ans += hashmap[target]
            
            hashmap[num] = hashmap.get(num, 0) + 1

        if hashmap.get(0) == n and goal == 0:
            return (n * (n + 1)) // 2

        return ans
