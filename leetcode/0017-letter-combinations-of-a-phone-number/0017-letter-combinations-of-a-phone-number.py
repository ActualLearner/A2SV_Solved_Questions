class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        N = len(digits)

        def backtrack(i, path):
            if i == N:
                ans.append("".join(path))
                return

            start = ord("a") + 3 * (int(digits[i]) - 2)
            end = start + 3

            if digits[i] == "7":
                end += 1
            elif digits[i] == "8":
                start += 1
                end += 1
            elif digits[i] == "9":
                start += 1
                end += 2

            for j in range(start, end):
                path.append(chr(j))
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return ans