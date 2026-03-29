# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        bigVal = 5 * (10**4)
        ans = 0

        # [isBST, subtree_min, subtree_max, subtree_sum]
        def backtrack(node):
            nonlocal ans
            if not node:
                return [True, bigVal, -bigVal, 0]
            
            left = backtrack(node.left)
            right = backtrack(node.right)
            
            curr = [True]

            if node.val > left[2] and node.val < right[1]:
                curr[0] = left[0] and right[0]
            else:
                curr[0] = False
            
            curr.append(min(left[1], node.val))
            curr.append(max(right[2], node.val))
            curr.append(left[3] + right[3] + node.val)
            
            if curr[0]:
                ans = max(ans, curr[3])

            return curr
            
        backtrack(root)
        return ans
