class Node:
    def __init__(self, val=-1, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularDeque:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.count = 0
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.count == self.k:
            return False

        curr = Node(value)

        if not self.head:
            self.head = curr
        
        if not self.tail:
            self.tail = curr
            self.count += 1
            return True

        self.tail.next = curr
        curr.prev = self.tail
        self.tail = curr
        self.count += 1

        return True

    def insertLast(self, value: int) -> bool:
        if self.count == self.k:
            return False

        curr = Node(value)
        if not self.tail:
            self.tail = curr
        
        if not self.head:
            self.head = curr
            self.count += 1
            return True

        self.head.prev = curr
        curr.next = self.head
        self.head = curr
        self.count += 1

        return True

    def deleteFront(self) -> bool:
        if not self.tail:
            return False
        
        if self.tail == self.head:
            self.tail = None
            self.head = None
            self.count -= 1
            return True

        prev = self.tail.prev
        self.tail = prev
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if not self.head:
            return False
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.count -= 1
            return True
        
        next_ = self.head.next
        self.head = next_
        self.count -= 1
        return True

    def getFront(self) -> int:
        if not self.tail:
            return -1
        
        return self.tail.val

    def getRear(self) -> int:
        if not self.head:
            return -1
        
        return self.head.val

    def isEmpty(self) -> bool:
        if not self.head and not self.tail:
            return True
        
        return False

    def isFull(self) -> bool:
        return self.count == self.k
        

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