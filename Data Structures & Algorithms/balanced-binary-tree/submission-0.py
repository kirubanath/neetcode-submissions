# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs_height_process(node):
            if not node:
                return 0
            
            left = dfs_height_process(node.left)
            right= dfs_height_process(node.right)

            height = 1 + max(left, right)
            
            nonlocal res
            res = res and (abs(left-right) <= 1)

            return height
        
        dfs_height_process(root)

        return res
        