class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hashmap = Counter(answers)
        ans = 0
        
        for key, value in hashmap.items():
            if key == 0:
                ans += value
            elif value >= key + 1:
                curr = -value // (key + 1)
                ans += (-curr)*(key + 1)
            else:
                ans += key + 1
            
        return ans