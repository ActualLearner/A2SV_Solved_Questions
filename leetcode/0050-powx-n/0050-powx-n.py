class Solution:
    def myPow(self, x: float, n: int) -> float:
        pos_n = n
        if n < 0:
            pos_n = abs(n)
            x = (1 / x)
        
        if pos_n == 0:
            return 1
        elif pos_n == 1:
            return x

        prod = 1 * (x if pos_n % 2 else 1)
        curr = self.myPow(x, pos_n // 2)
        prod *= curr * curr
        
        return prod
    