class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
        n = abs(n)

        def pow(x, n):
            if n == 0:
                return 1
            
            curr = pow(x, n // 2)
            if n % 2:
                return x * curr * curr
            
            return curr * curr  

        return pow(x, n)