# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def sum(node):
            if not node:
                return [True, 0, float("inf"), float("-inf")]

            left = sum(node.left)
            right = sum(node.right)

            if left[0] and right[0] and node.val > left[3] and node.val < right[2]:
                sum_ = left[1] + right[1] + node.val
                self.ans = max(self.ans, sum_)
                return [True, sum_, min(left[2], node.val), max(right[3], node.val)]
            
            return [False, max(left[1], right[1])]
            

        sum(root)
        return self.ans
        