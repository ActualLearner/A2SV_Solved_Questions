class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(i, path):
            if len(path) == k:
                ans.append(path[:])
                return
            elif i == n + 1 or len(path) + (n - i + 1) < k:
                return
            
            path.append(i)
            backtrack(i + 1, path)
            path.pop()
            backtrack(i + 1, path)
        
        backtrack(1, [])
        return ans