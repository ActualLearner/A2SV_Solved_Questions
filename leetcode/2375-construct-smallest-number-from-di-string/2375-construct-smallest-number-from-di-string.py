class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        result = ""

        def backtrack(path, index):
            nonlocal result
            
            if index == n + 1:
                result = "".join(map(str, path[:]))
                return True
            
            for i in range(1, 10):
                if i in path:
                    continue
                elif index == 0:
                    pass
                elif pattern[index - 1] == "I" and i <= path[-1]:
                    continue
                elif pattern[index - 1] == "D" and i >= path[-1]:
                    continue
                
                path.append(i)
                if backtrack(path, index + 1):
                    return True
                path.pop()
            
            return False

        backtrack([], 0)
        return result