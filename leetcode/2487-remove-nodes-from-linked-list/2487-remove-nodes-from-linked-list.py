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

            if not new_head:
                new_head = head
                head.next = None
            elif head.val < new_head.val:
                head.next = new_head
                new_head = head
            else:
                curr = new_head
                while curr and curr.val < head.val:
                    curr = curr.next
                
                new_head = head
                head.next = curr
            
            head = temp
        
        # reverse 13, 1, 8
        ans = None
        while new_head:
            temp = new_head.next
            new_head.next = ans
            ans = new_head
            new_head = temp
                
        return ans
                