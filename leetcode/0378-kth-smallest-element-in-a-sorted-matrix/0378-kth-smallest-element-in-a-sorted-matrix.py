class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []

        for j in range(min(n, k)):
            for i in range(min(n, k)):
                heappush(heap, matrix[i][j])
        
        ans = heap[0]
        while heap and k > 0:
            k -= 1
            ans = heappop(heap)
        
        return ans

        

