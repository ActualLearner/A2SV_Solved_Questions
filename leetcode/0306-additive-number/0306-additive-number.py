class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        valid = False

        def find(path, s):
            nonlocal valid

            if valid:
                return
            elif len(path) > 2:
                for i in range(2, len(path)):
                    if path[i] != path[i - 1] + path[i - 2]:
                        return
                
                if s == n:
                    valid = True
                    return
            
            for i in range(s, len(num)):
                if i != s and num[s] == "0":
                    continue
                path.append(int(num[s:i + 1]))
                find(path, i + 1)
                path.pop()
            
        find([], 0)
        return valid
