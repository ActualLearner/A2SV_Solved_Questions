# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:

        def sum(parent, node):
            if not node:
                return 0
                
            left = sum(node, node.left)
            right = sum(node, node.right)
            sum_ = left + right

            if parent and parent.val % 2 == 0:
                sum_ += (node.left.val if node.left else 0)
                sum_ += (node.right.val if node.right else 0)

            return sum_

        return sum(None, root)