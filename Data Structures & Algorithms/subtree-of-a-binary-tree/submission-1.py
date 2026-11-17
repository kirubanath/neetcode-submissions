# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Idea : Get a list of string representation of the two trees!
Just compare if the list of a sublist or string is a substring (subroot to root)
"""
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def tree_rep(node):
            
            tree = []
            stack = [node]

            while stack:

                node = stack.pop()

                if not node:
                    tree.append("None")
                
                else:
                    tree.append(node.val)

         
                    stack.append(node.left)        
                    stack.append(node.right)
            
            return tree
        
        root_tree = tree_rep(root)
        sub_tree = tree_rep(subRoot)

        print(root_tree, sub_tree)

        
        r = len(sub_tree)
        while r <= len(root_tree):

            # process
            if root_tree[r-len(sub_tree) : r] == sub_tree:
                return True

            # increase
            r+=1
        
        return False





        