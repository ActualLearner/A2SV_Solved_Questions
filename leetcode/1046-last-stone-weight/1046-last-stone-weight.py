class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapify(stones)
        while len(stones) > 1:
            s1 = - heappop(stones)
            s2 = - heappop(stones)
            if s1 > s2:
                heappush(stones, s2 - s1)
        
        return -stones[0] if stones else 0