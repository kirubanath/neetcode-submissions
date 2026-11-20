# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Simple inorder traversal will give us the answer since BST
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        order = []

        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            order.append(root.val)
            
            if len(order) >=k:
                return 
            
            dfs(root.right)
        
        dfs(root)
        
        return order[k-1] 


        