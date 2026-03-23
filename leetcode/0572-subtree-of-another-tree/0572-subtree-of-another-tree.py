# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def traverse(curr1, curr2):
            if not curr1 and not curr2:
                return True
            elif (not curr1 or not curr2) or curr1.val != curr2.val:
                return False
            
            return traverse(curr1.left, curr2.left) and traverse(curr1.right, curr2.right)
        

        nodes = []

        def find(curr, value):
            if not curr:
                return None
            
            nonlocal nodes

            if value == curr.val:
                nodes.append(curr)
            
            find(curr.left, value)
            find(curr.right, value)

            return None
        
        find(root, subRoot.val)

        if not nodes:
            return False

        return any([traverse(node, subRoot) for node in nodes])