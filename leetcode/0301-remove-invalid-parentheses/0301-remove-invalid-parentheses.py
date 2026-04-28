class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)
        stack = []
        bad = {"(": 0, ")": 0}

        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                while stack and stack[-1] != "(":
                    bad[stack.pop()] += 1

                if not stack:
                    bad[char] += 1
                else:
                    stack.pop()
        
        for elem in stack:
            bad[elem] += 1

        def isValid(arr):
            stack = []
            for char in arr:
                if char == "(":
                    stack.append(char)
                elif char == ")":
                    if not stack or stack[-1] != "(":
                        return False
                    
                    stack.pop()
            
            if stack:
                return False
            
            return True

        ans = set()
        def bruteforce(path, i, bad):
            if i == n:
                if bad["("] + bad[")"] <= 0 and isValid(path):
                    ans.add("".join(path))
                
                return
            
            if s[i] in bad and bad[s[i]] > 0:
                bad[s[i]] -= 1
                bruteforce(path, i + 1, bad)
                bad[s[i]] += 1
            
            path.append(s[i])
            bruteforce(path, i + 1, bad)
            path.pop()


        bruteforce([], 0, bad)
        return list(ans)