# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        curr = head

        while curr != None:
            nums.append(curr.val)
            curr = curr.next
        
        curr = head
        for num in nums[::-1]:
            curr.val = num
            curr = curr.next

        return head