class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = []
        min_ = nums[0]

        for i, num in enumerate(nums[1:]):

            while stack and stack[-1][0] <= num:
                stack.pop()
            
            if stack and num > stack[-1][1]:
                return True
            
            stack.append([num, min_])
            min_ = min(min_, num)
        
        return False

