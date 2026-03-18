class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.tail = self.head

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.tail.next = new_node
        new_node.prev = self.tail

        self.tail = new_node

    def back(self, steps: int) -> str:
        while self.tail.prev and steps != 0:
            self.tail = self.tail.prev
            steps -= 1
        
        return self.tail.val

    def forward(self, steps: int) -> str:
        while self.tail.next and steps != 0:
            self.tail = self.tail.next
            steps -= 1
        
        return self.tail.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)