# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0

        def path_sum(node, path):
            nonlocal ans
            if not node:
                return path

            # add curr node or don't then move to choice 2
            path.append(node.val)
            if sum(path) == targetSum:
                ans += 1
            path_sum(node.right, path)
            path_sum(node.left, path)
            path.pop()

            if not path:
                path_sum(node.right, path)
                path_sum(node.left, path)
        
        path_sum(root, [])
        return ans
