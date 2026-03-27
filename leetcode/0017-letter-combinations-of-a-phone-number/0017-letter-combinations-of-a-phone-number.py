class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        n = len(digits)

        def backtrack(path, index):
            if index == n:
                result.append("".join(path[:]))
                return
            
            start = (int(digits[index]) - 2) * 3
            end = (int(digits[index]) - 1) * 3

            if digits[index] == '7':
                end += 1
            elif digits[index] == '8':
                start += 1
                end += 1
            elif digits[index] == '9':
                start += 1
                end += 2

            for i in range(start, end):
                path.append(chr(ord("a") + i))
                backtrack(path, index + 1)
                path.pop()
            
        backtrack([], 0)
        return result
