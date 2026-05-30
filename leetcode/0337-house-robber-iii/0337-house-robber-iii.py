# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            curr_rob = node.val + left[1] + right[1]
            curr_dont_rob = max(left) + max(right)
            return (curr_rob, curr_dont_rob)
        
        ans = dfs(root)
        return max(ans)