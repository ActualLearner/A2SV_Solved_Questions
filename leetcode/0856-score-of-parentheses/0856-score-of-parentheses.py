class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                num = 0
                while stack and stack[-1] != "(":
                    val = stack.pop()
                    if isinstance(val, int):
                        num += val
                
                stack.pop()
                stack.append(2 * num if num != 0 else 1)
        
        return sum(stack)