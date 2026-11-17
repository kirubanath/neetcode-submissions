# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Same idea as solution 2 but with a string.
In a list there is already a natural separator between elements. Since we wont have here we add it as $ and None as # 
USE ONLY DFS and not BFS
DFS preserves the subtree as is..but BFS preserves the level!
"""
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def tree_rep(node):
    
            ts = ""
            que = [node]

            while que:

                node = que.pop()

                if not node:
                    ts += "#"
                
                else:
                    ts += f"${node.val}"
                    que.append(node.left)
                    que.append(node.right)
            
            return ts
        
        rs = tree_rep(root)
        ss = tree_rep(subRoot)

        print(rs,ss)

        return ss in rs




        