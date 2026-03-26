class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(path, index):
            if len(path) == k:
                res.append(path[:])
                return
            elif index == n + 1:
                return
            

            path.append(index)
            backtrack(path, index + 1)
            path.pop()

            backtrack(path, index + 1)
        
        backtrack([], 1)
        return res
