class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        ans = float('inf')

        def backtrack(sums, index):
            nonlocal ans

            if index == n:
                ans = min(ans, max(sums))
                return

            for i in range(k):
                sums[i] += cookies[index]
                backtrack(sums, index + 1)
                sums[i] -= cookies[index]
        
        backtrack([0 for _ in range(k)], 0)
        return ans