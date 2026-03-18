# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        even = head

        if not curr:
            return curr

        idx = 0
        while curr.next:
            idx += 1
            if idx % 2 == 0:
                temp = curr.next.next
                curr.next.next = even.next
                even.next = curr.next
                curr.next = temp

                even = even.next
            else:
                curr = curr.next
        
        return head


