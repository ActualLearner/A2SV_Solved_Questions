# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_ = float("-inf")

        def traverse(node):
            nonlocal max_
            if not node:
                return float("-inf")
            
            right = traverse(node.right)
            left = traverse(node.left)

            curr_sum = left + right + node.val
            right_path = right + node.val
            left_path = left + node.val

            max_ = max(max_, curr_sum, left_path, right_path, node.val)
            best = max(left, right)
            return max((best if best != float("-inf") else 0) + node.val, node.val)
        
        traverse(root)
        return max_
