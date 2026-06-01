class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        elif n == 2:
            return 1
        
        prev1, prev2, prev3 = 0, 1, 1
        for _ in range(n - 2):
            curr = prev1 + prev2 + prev3
            prev1, prev2 = prev2, prev3
            prev3 = curr
        
        return prev3
        
            