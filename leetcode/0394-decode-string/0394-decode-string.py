class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        stack = []

        for char in s:
            if char == "]":
                # pop until we find a number
                # how to extract multi digit number?

                curr = []
                while stack and stack[-1] != "[":
                    curr.append(stack.pop())
                
                if stack:
                    stack.pop()

                val = []
                while stack and stack[-1].isdigit():
                    val.append(stack.pop())

                value = int("".join(val[::-1])) if val else 1

                # append value amount of times
                for _ in range(value):
                    for i in range(len(curr) - 1, -1, -1):
                        stack.append(curr[i])
            else:
                stack.append(char)

        return "".join(stack)
            