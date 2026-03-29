# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(-1)

        def backtrack(node):
            nonlocal new_head
            if not node:
                return new_head
            
            next_ = backtrack(node.next)
            next_.next = node

            return node
        
        backtrack(head)
        if head:
            head.next = None
        return new_head.next