# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(arr):
            if not arr:
                return None
            
            max_ = 0
            for i in range(len(arr)):
                if arr[i] > arr[max_]:
                    max_ = i
            
            left = build(arr[:max_])
            right = build(arr[max_ + 1:])

            return TreeNode(arr[max_], left, right)

        return build(nums)