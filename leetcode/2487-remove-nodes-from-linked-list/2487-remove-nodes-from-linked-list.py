# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        while head:
            temp = head.next
            head.next = new_head
            new_head = head
            head = temp
        
        ans = tail = None
        while new_head:
            temp = new_head.next
            if not ans:
                ans = tail = new_head
                ans.next = None
            elif new_head.val >= tail.val:
                tail.next = new_head
                new_head.next = None
                tail = new_head
            
            new_head = temp
        
        new_head = None
        while ans:
            temp = ans.next
            ans.next = new_head
            new_head = ans
            ans = temp

        return new_head
                