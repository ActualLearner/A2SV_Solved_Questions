class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        list_ = ["a", "b", "c"]
        # n = 2

        def backtrack(path, index):
            if index == n:
                if len(path) == n:
                    result.append("".join(path[:]))
                return
            
            for char in list_:
                if not path or char != path[-1]:
                    path.append(char)
                    backtrack(path, index + 1)
                    path.pop()
        
        backtrack([], 0)

        if k > len(result):
            return ""
        return result[k - 1]
