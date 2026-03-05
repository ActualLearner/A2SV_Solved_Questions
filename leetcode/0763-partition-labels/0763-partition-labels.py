class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)
        left = 0
        curr = {}
        ans = []

        for right in range(len(s)):
            char = s[right]
            curr[char] = curr.get(char, 0) + 1

            valid = True
            for key, value in curr.items():
                if value < counter[key]:
                    valid = False
                    break
            
            if valid:
                ans.append(right - left + 1)
                curr = {}
                left = right + 1
            
        return ans