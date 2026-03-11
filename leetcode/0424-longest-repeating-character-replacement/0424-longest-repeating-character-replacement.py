class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        max_ = 0
        hashmap = {}
        left = 0

        for right in range(n):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1

            while (right - left + 1) - max(hashmap.values()) > k:
                hashmap[s[left]] = hashmap.get(s[left], 0) - 1
                left += 1

            max_ = max(max_, right - left + 1)
        
        return max_