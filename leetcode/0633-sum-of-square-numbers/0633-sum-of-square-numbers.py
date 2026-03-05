class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left = 0
        right = int(c ** 0.5)

        while left < right:
            sum_ = (left ** 2) + (right ** 2)  
            if sum_ < c:
                left += 1
            elif sum_ > c:
                right -= 1
            else:
                break
        
        if (left ** 2) + (right ** 2) == c:
            return True
        else:
            return False