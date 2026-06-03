class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(wage)
        arr = []

        for i in range(n):
            arr.append((wage[i] / quality[i], wage[i], quality[i])) 
        
        arr.sort()
        ans = float("inf")
        heap = []
        sum_ = 0
        
        for i in range(n):
            if len(heap) < k - 1:
                heappush(heap, -arr[i][2])
                sum_ += arr[i][2]
                continue
            
            total = sum_ + arr[i][2]
            ans = min(ans, total * arr[i][0])

            if heap and arr[i][2] < -heap[0]:
                temp = heappop(heap)
                heappush(heap, -arr[i][2])
                sum_ += temp
                sum_ += arr[i][2]

        return ans
            
