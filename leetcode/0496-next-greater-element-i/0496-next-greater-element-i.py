class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N = len(nums2)
        stack = []
        hashmap = {}

        for i in range(N):
            while stack and nums2[i] > stack[-1]:
                hashmap[stack[-1]] = nums2[i]
                stack.pop()
            
            stack.append(nums2[i])
        
        ans = []
        for num in nums1:
            if num not in hashmap:
                ans.append(-1)
            else:
                ans.append(hashmap[num])
        
        return ans