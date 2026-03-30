class MyCircularDeque:

    def __init__(self, k: int):
        self.list = [-1] * k
        self.front = 0
        self.rear = k - 1
        self.count = 0

    def insertFront(self, value: int) -> bool:
        index_front = (self.front - 1) % len(self.list)
        if self.list[index_front] != -1:
            return False
        
        self.list[index_front] = value
        self.front -= 1
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        index_rear = (self.rear + 1) % len(self.list)
        if self.list[index_rear] != -1:
            return False
        
        self.list[index_rear] = value
        self.rear += 1
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        index = self.front % len(self.list)
        if self.list[index] == -1:
            return False
        
        self.list[index] = -1
        self.front += 1
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        index = self.rear % len(self.list)
        if self.list[index] == -1:
            return False
        
        self.list[index] = -1
        self.rear -= 1
        self.count -= 1
        return True

    def getFront(self) -> int:
        return self.list[self.front % len(self.list)]

    def getRear(self) -> int:
        return self.list[self.rear % len(self.list)]
        

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == len(self.list)


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()