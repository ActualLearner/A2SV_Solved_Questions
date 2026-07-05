class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def backtrack(i, path):
            if i == n:
                ans.append(path[:])
            
            for num in nums:
                if num in path:
                    continue
                
                path.append(num)
                backtrack(i + 1, path)
                path.pop()
            
        backtrack(0, [])
        return ans