class Solution:
    def tribonacci(self, n: int) -> int:
        i = 3
        ans = 0
        prev = [0, 1, 1]

        if n <= 2:
            return prev[n]

        while i <= n:
            curr = sum(prev)
            prev[0] = prev[1]
            prev[1] = prev[2]
            prev[2] = curr
            i += 1
        
        return prev[-1]
            


            