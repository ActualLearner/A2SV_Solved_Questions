class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        N = len(nums)
        left = 0
        hashmap = {}
        val1 = 0
        val2 = 0

        for right in range(N):
            hashmap[nums[right]] = hashmap.get(nums[right], 0) + 1

            while left <= right and len(hashmap) > k:
                hashmap[nums[left]] = hashmap.get(nums[left], 0) - 1

                if hashmap[nums[left]] <= 0:
                    del hashmap[nums[left]]
                
                left += 1

            val2 += (right - left + 1)
        
        left = 0
        hashmap = {}

        for right in range(N):
            hashmap[nums[right]] = hashmap.get(nums[right], 0) + 1

            while left <= right and len(hashmap) > k - 1:
                hashmap[nums[left]] = hashmap.get(nums[left], 0) - 1
                if hashmap[nums[left]] <= 0:
                    del hashmap[nums[left]]
                
                left += 1
            
            val1 += (right - left + 1)
            
        return val2 - val1