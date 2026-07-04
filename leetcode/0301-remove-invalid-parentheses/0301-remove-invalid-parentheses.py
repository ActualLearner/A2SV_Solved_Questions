class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)
        ans = set()
        right = left = 0

        for char in s:
            if char == "(":
                right += 1
            elif char == ")":
                left += 1 if right == 0 else 0
                right -= 1 if right > 0 else 0
            
        if right + left == 0:
            return [s]
        
        def backtrack(i, right_b, left_b, path):
            if i == n:
                if right_b + left_b != 0:
                    return

                right = left = 0
                for char in path:
                    if char == "(":
                        right += 1
                    elif char == ")":
                        left += 1 if right == 0 else 0
                        right -= 1 if right > 0 else 0

                if left + right == 0:
                    ans.add("".join(path))

                return

            path.append(s[i])
            backtrack(i + 1, right_b, left_b, path)
            path.pop()

            if right_b > 0 and s[i] == "(":
                backtrack(i + 1, right_b - 1, left_b, path)
            elif left_b > 0 and s[i] == ")":
                backtrack(i + 1, right_b, left_b - 1, path)
        
        backtrack(0, right, left, [])
        return list(ans)
