class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        ans = []

        for char in order:
            ans.extend(char * counter[char])
            del counter[char]
        
        for key, value in counter.items():
            ans.extend(key * value)
        
        return "".join(ans)