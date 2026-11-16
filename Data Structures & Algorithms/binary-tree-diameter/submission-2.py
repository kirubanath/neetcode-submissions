# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Idea: DFS processes everything from ground up. So we process leaf first and then move up
We can just get the diameter of the leaf node..then keep moving up and upate the diameter of all the nodes..then just get the max! 
diamter = left height + right height
cur_height = 1 + max(left,right!)
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0

        def dfs_height_process(node):
            if not node:
                return 0

            left = dfs_height_process(node.left) 
            right = dfs_height_process(node.right) 

            # While we are here..we can get the cur diam as well!
            diam = left + right

            # We can then just udpate the global res
            nonlocal res
            res = max(res, diam)

            return 1 + max(left,right)
        
        dfs_height_process(root)

        return res
        



        