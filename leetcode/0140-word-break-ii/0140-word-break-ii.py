class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = set()
        min_len = 0
        max_len = 0
        word_set = set(wordDict)

        for word in wordDict:
            min_len = min(min_len, len(word))
            max_len = max(max_len, len(word))

        def bruteforce(path, i):
            nonlocal ans
            nonlocal word_set
            nonlocal min_len
            nonlocal max_len

            if i >= len(s):
                total = 0
                for word in path:
                    total += len(word)

                if total == len(s):
                    ans.add(" ".join(path))
                
                return
            

            for j in range(min_len, max_len + 1):
                if len(s) - (i + j) + 1 < min_len:
                    continue
                elif s[i:i+j] not in word_set:
                    continue
                
                path.append(s[i:i+j])
                bruteforce(path, i + j)
                path.pop()
            
            return

        bruteforce([], 0)
        return list(ans)
