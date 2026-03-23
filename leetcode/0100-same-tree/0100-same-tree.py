# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q or p.val != q.val:
            return False
        
        def traverse(curr1, curr2):
            if not curr1 and not curr2:
                return True
            elif not curr1 or not curr2 or curr1.val != curr2.val:
                return False
            
            return traverse(curr1.left, curr2.left) and traverse(curr1.right, curr2.right)
        
        return traverse(p, q)