# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        mp = {val:index for index, val in enumerate(inorder)}
        self.pre_idx = 0

        def dfs(l,r):

            if l > r:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx+=1
            in_idx = mp[root_val]

            root = TreeNode(root_val)
            root.left = dfs(l,in_idx-1)
            root.right = dfs(in_idx+1,r)

            return root
        
        return dfs(0,len(inorder)-1)



