class Solution:
    def lastRemaining(self, n: int) -> int:
        ans = 1
        interval = 1
        forward = True

        while n > 1:
            if forward or n % 2 == 1:
                ans += interval

            n //= 2
            interval *= 2
            forward = not forward
        
        return ans