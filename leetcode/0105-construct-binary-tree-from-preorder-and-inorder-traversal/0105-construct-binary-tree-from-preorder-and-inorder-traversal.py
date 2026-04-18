# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        N = len(preorder)
        hashmap_in = {}

        for i in range(N):
            hashmap_in[inorder[i]] = i

        def build(pleft, pright, left, right):
            if pleft > pright or left > right:
                return None
            
            root = TreeNode(preorder[pleft])
            mid = hashmap_in[preorder[pleft]]
            left_size = mid - left

            root.left = build(pleft + 1, pleft + left_size, left, mid - 1)
            root.right = build(pleft + left_size + 1, pright, mid + 1, right)
            return root
        
        root = build(0, N - 1, 0, N - 1)
        return root