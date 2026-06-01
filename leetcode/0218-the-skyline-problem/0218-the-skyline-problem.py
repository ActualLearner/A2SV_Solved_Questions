class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        arr = []

        for start, end, h in buildings:
            arr.append((start, -h, end))
            arr.append((end, 0, 0))

        arr.sort()

        ans = []
        max_heap = [(0, float('inf'))]
        prev_height = 0

        for start, h, end in arr:
            if h < 0:
                heappush(max_heap, (h, end))

            while max_heap[0][1] <= start:
                heappop(max_heap)

            curr_height = -max_heap[0][0]

            if curr_height != prev_height:
                ans.append([start, curr_height])
                prev_height = curr_height

        return ans