class Solution:
    def splitString(self, s: str) -> bool:
        
        def split(path, i):
            if i == len(s):
                for i in range(1, len(path)):
                    if int(path[i - 1]) - int(path[i]) != 1:
                        return False
                
                return len(path) >= 2
            
            for j in range(i, len(s)):
                path.append(s[i:j + 1])
                if split(path, j + 1):
                    return True
                path.pop()

            return False
            
        return split([], 0)