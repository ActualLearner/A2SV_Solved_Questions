class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        ans = []            
        heap = []
        for word, count in freq.items():
            heappush(heap, (-count, word))
        
        while heap and k > 0:
            count, word = heappop(heap)
            ans.append(word)
            k -= 1
        return ans