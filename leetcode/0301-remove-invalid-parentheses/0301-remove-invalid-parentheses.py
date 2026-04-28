class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)
        left_b, right_b = 0, 0

        for char in s:
            if char == "(":
                left_b += 1
            elif char == ")":
                if left_b > 0:
                    left_b -= 1
                else:
                    right_b += 1


        ans = set()
        def bruteforce(path, i, left, right, count):
            if i == n:
                if left + right + count == 0:
                    ans.add("".join(path))
                return 

            if s[i] == "(" and left > 0:                    
                bruteforce(path, i + 1, left - 1, right, count)
            elif s[i] == ")" and right > 0:
                bruteforce(path, i + 1, left, right - 1, count)
            
            if s[i] == "(":
                count += 1
            elif s[i] == ")":
                count -= 1
            
            if count < 0:
                return
                
            path.append(s[i])
            bruteforce(path, i + 1, left, right, count)
            path.pop()


        bruteforce([], 0, left_b, right_b, 0)
        return list(ans)