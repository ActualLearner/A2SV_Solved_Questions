class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ans = []
        prefix = [0] * (len(s) + 1)

        for left, right, drxn in shifts:
            if drxn:
                prefix[left] += 1
                prefix[right + 1] -= 1

            if not drxn:
                prefix[left] -= 1
                prefix[right + 1] += 1
            
        for i in range(1, len(s) + 1):
            prefix[i] += prefix[i - 1]
        
        for i in range(len(s)):
            char = ord(s[i]) - ord('a')
            idx = char + prefix[i] 
            ans.append(chr(ord('a') + idx % 26))
        
        return "".join(ans)