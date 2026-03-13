class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hashmap = {5: 0, 10:0, 20:0}

        for num in bills:
            hashmap[num] += 1
            change = num - 5

            while change > 0:
                if change >= 10 and hashmap[10] >= 1:    
                    hashmap[10] -= 1
                    change -= 10
                elif change >= 5:
                    hashmap[5] -= 1
                    change -= 5
            
            if hashmap[5] < 0 or hashmap[10] < 0:
                return False
        
        return True
            