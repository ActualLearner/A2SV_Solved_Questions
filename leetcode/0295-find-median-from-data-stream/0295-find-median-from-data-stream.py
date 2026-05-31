class MedianFinder:

    def __init__(self):
        self.heapleft = []
        self.heapright = []

    def addNum(self, num: int) -> None:
        heappush(self.heapleft, -num)
        heappush(self.heapright, -heappop(self.heapleft))

        if len(self.heapleft) < len(self.heapright):
            heappush(self.heapleft, -heappop(self.heapright))

    def findMedian(self) -> float:
        if len(self.heapleft) > len(self.heapright):
            return -self.heapleft[0]
        
        return (self.heapright[0] - self.heapleft[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()