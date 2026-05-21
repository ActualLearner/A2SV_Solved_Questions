class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        arr = [(t[0], t[1], i) for i, t in enumerate(tasks)]
        arr.sort(key=lambda x: x[0])
        idx, time = 0, 0
        ans = []
        heap = []

        while heap or idx < n:
            while idx < n and time >= arr[idx][0]:
                heappush(heap, (arr[idx][1], arr[idx][2]))
                idx += 1

            if not heap:
                time = arr[idx][0] if idx < n else time
                continue
            
            pt, i = heappop(heap)
            time += pt
            ans.append(i)
    
        return ans